#!/usr/bin/env python
import random
import itertools
import requests
from time import sleep
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PySide6.QtCore import (QRunnable, QThreadPool, Signal, QObject, Slot, Qt)

from ui.Ui_leakscan import Ui_Form

from utility import USER_AGENT, getLastDate, read_dir_file, web_alive, get_proxy_config, read_url_file, log_write

# 定义信号传递的对象
class LeakScanSignals(QObject):
    leak_scan_signal = Signal(str)

# 定义实际的任务
class LeakScanWorker(QRunnable):

    def __init__(self, url, headers=None, proxies=None, delay=0):
        super().__init__()
        self.url = url
        self.headers = headers
        self.proxies = proxies
        self.delay = delay
        self.signals = LeakScanSignals()

    # 单个扫描
    def single_scan(self):
        try:
            r = requests.get(url=self.url, headers=self.headers, proxies=self.proxies, timeout=6, allow_redirects=False)
            sleep(self.delay)
            if ((r.status_code == 200) and ('need login' not in r.text) and ('禁止访问' not in r.text) and ('无访问权限' not in r.text) and ('认证失败' not in r.text)):
                return f'[+] Status code{r.status_code} --- info leak --> {self.url}'
            elif (r.status_code == 200):
                return f'[+] Status code{r.status_code} --- can not get info --> {self.url}'
            else:
                return f'[-] Status code{r.status_code} --- no leak'
        except:
            return f'[-] Can not connect --> {self.url}'

    def run(self):
        res = self.single_scan()
        # 任务完成后发出信号
        self.signals.leak_scan_signal.emit(f'{getLastDate()} {res}')


class leakScanPage(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__()

        self.setupUi(self)
        self.parent = parent
        self.proxies = None

        self.leak_scan_pool = QThreadPool()
        
        self.loadUrlPushButton.clicked.connect(self.load_url)
        self.startPushButton.clicked.connect(self.start_button)
        self.agencyCheckBox.stateChanged.connect(self.proxy_test)


    # 代理链接测试
    def proxy_test(self):
        if self.agencyCheckBox.checkState() == Qt.CheckState.Checked:
            proxy_config = get_proxy_config('./config.ini')
            if web_alive('http://www.baidu.com', proxy_config) == True:
                self.agencyCheckBox.setCheckState(Qt.Checked)
                self.proxies = proxy_config
                QMessageBox.information(self, 'info', 'Connect Success')
            else:
                self.agencyCheckBox.setCheckState(Qt.Unchecked)
                QMessageBox.information(self, 'info', 'Connect Unsuccess')

    # 读取url文件
    def load_url(self):
        # 打开文件对话框，获取文件路径
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt);;All Files (*)')

        if file_path:
            try:
                # 读取文件内容
                url_list = read_url_file(file_path)
                for url in url_list:
                    self.urlPlainTextEdit.appendPlainText(url.strip())

            except Exception as e:
                # 如果读取文件时出错，显示错误信息
                QMessageBox.critical(self, 'Error', f'Failed to read file: {e}', QMessageBox.Ok)

    # 开始按钮
    def start_button(self):
        url_list = self.urlPlainTextEdit.toPlainText().split('\n') # 获取url列表
        if len(url_list) > 0:
            self.startPushButton.setEnabled(False)
            self.logPlainTextEdit.clear()
            self.leak_scan_pool.setMaxThreadCount(self.threadCountSpinBox.value()) # 设置线程数
            dir_list = read_dir_file('dir.txt') # 获取目录列表
            self.leak_scan_count = len(url_list) * len(dir_list) # 任务总数
            self.leak_scan_done_tasks = 0
            self.progressBar.setRange(0, self.leak_scan_count) # 设置进度条范围
            user_agent = random.choice(USER_AGENT) # 随机获取user-agent
            headers = {'User-Agent': user_agent}
            delay = self.delayDoubleSpinBox.value() # 获取延迟

            for url, leak_dir in itertools.product(url_list, dir_list):
                url = url.strip().strip('/')
                target_url = url + leak_dir
                worker = LeakScanWorker(url=target_url, headers=headers, proxies=self.proxies, delay=delay)
                worker.signals.leak_scan_signal.connect(self.show_log)
                self.leak_scan_pool.start(worker)


    @Slot(str)
    def show_log(self, info):
        log_write(f"[{getLastDate()}] {info}")
        if '[+]' in info:
            self.logPlainTextEdit.appendPlainText(info)
        else:
            if len(info) >= 60:
                self.scanStatusLabel.setText(info[:59] + '...')
            else:
                self.scanStatusLabel.setText(info)
        
        self.leak_scan_done_tasks += 1
        self.progressBar.setValue(self.leak_scan_done_tasks)

        if self.leak_scan_done_tasks == self.leak_scan_count:
            self.logPlainTextEdit.appendPlainText('Scanning Done')
            self.scanStatusLabel.setText('No scanning')
            self.startPushButton.setEnabled(True)

    # 关闭事件
    def closeEvent(self, event):
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication([])
    window = leakScanPage()
    window.show()
    app.exec()