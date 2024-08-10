#!/usr/bin/env python
import random
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PySide6.QtCore import (QThread, Signal, Slot, Qt)

from ui.Ui_vuldetect import Ui_Form
from utility import getLastDate, web_alive, get_proxy_config, read_url_file, log_write, USER_AGENT
from poc_list import JeeSpringCloud_2023, CVE_2022_22978, CVE_2022_22965, CVE_2022_22963, CVE_2022_22947, CVE_2021_21234, CVE_2018_1273, SnakeYAML_2021_rce, Jolokia_2020_rce, Eureka_Xstream_2021_rce

class PocThread(QThread):

    poc_signal = Signal(str)

    def __init__(self, proxies):
        super().__init__()
        self.proxies = proxies

    # poc选择
    def set_poc(self, poc_name):
        self.poc_name = poc_name
    
    # 设置url列表
    def set_url_list(self, urls):
        self.urls = urls

    def run(self):
        user_agent = random.choice(USER_AGENT)
        for url in self.urls:
            if self.poc_name == 'ALL':
                self.poc_signal.emit(JeeSpringCloud_2023.poc(url, user_agent, self.proxies))
                self.poc_signal.emit(CVE_2022_22978.poc(url, user_agent, self.proxies))
                self.poc_signal.emit(CVE_2022_22965.poc(url, user_agent, self.proxies))
                self.poc_signal.emit(CVE_2022_22963.poc(url, user_agent, self.proxies))
                self.poc_signal.emit(CVE_2022_22947.poc(url, user_agent, self.proxies))
                self.poc_signal.emit(CVE_2021_21234.poc(url, user_agent, self.proxies))
                self.poc_signal.emit(CVE_2018_1273.poc(url, user_agent, self.proxies))
                self.poc_signal.emit(SnakeYAML_2021_rce.poc(url, user_agent, self.proxies))
                self.poc_signal.emit(Jolokia_2020_rce.poc(url, user_agent, self.proxies))
                self.poc_signal.emit(Eureka_Xstream_2021_rce.poc(url, user_agent, self.proxies))
            elif self.poc_name == 'JeeSpringCloud_2023':
                self.poc_signal.emit(JeeSpringCloud_2023.poc(url, user_agent, self.proxies))
            elif self.poc_name == 'CVE_2022_22978':
                self.poc_signal.emit(CVE_2022_22978.poc(url, user_agent, self.proxies))
            elif self.poc_name == 'CVE_CVE_2022_22965':
                self.poc_signal.emit(CVE_2022_22965.poc(url, user_agent, self.proxies))
            elif self.poc_name == 'CVE_2022_22963':
                self.poc_signal.emit(CVE_2022_22963.poc(url, user_agent, self.proxies))
            elif self.poc_name == 'CVE_2022_22947':
                self.poc_signal.emit(CVE_2022_22947.poc(url, user_agent, self.proxies))
            elif self.poc_name == 'CVE_2021_21234':
                self.poc_signal.emit(CVE_2021_21234.poc(url, user_agent, self.proxies))
            elif self.poc_name == 'CVE_2018_1273':
                self.poc_signal.emit(CVE_2018_1273.poc(url, user_agent, self.proxies))
            elif self.poc_name == 'SnakeYAML_2021_rce':
                self.poc_signal.emit(SnakeYAML_2021_rce.poc(url, user_agent, self.proxies))
            elif self.poc_name == 'Jolokia_2020_rce':
                self.poc_signal.emit(Jolokia_2020_rce.poc(url, user_agent, self.proxies))
            elif self.poc_name == 'Eureka_Xstream_2021_rce':
                self.poc_signal.emit(Eureka_Xstream_2021_rce.poc(url, user_agent, self.proxies))


class vulDetectPage(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__()

        self.setupUi(self)
        self.parent = parent
        self.proxies = None

        self.poc_dect = PocThread(self.proxies)
        self.poc_dect.poc_signal.connect(self.show_log)

        self.loadUrlPushButton.clicked.connect(self.load_url)
        self.agencyCheckBox.stateChanged.connect(self.proxy_test)
        self.detectPushButton.clicked.connect(self.start_button)


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

    # 开始检测
    def start_button(self):
        poc_name = self.comboBox.currentText()
        self.poc_dect.set_poc(poc_name)
        self.poc_dect.set_url_list(self.urlPlainTextEdit.toPlainText().split('\n'))
        self.poc_dect.start()

    @Slot(str)
    def show_log(self, info):
        log_write(f"[{getLastDate()}] {info}")
        self.logPlainTextEdit.appendPlainText(info)
        

    # 关闭事件
    def closeEvent(self, event):
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication([])
    window = vulDetectPage()
    window.show()
    app.exec()