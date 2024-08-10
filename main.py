from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import (QRunnable, QThreadPool, Signal, QObject, Slot, Qt)

from ui.Ui_spring import Ui_Form
from leak_scan_page import leakScanPage
from vul_detect_page import vulDetectPage


class mainPage(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.leak_scan = leakScanPage(self)
        self.tabWidget.addTab(self.leak_scan, 'LeakScan')

        self.vul_detect = vulDetectPage(self)
        self.tabWidget.addTab(self.vul_detect, 'VulDetect')



    # 关闭事件
    def closeEvent(self, event):
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication([])
    window = mainPage()
    window.show()
    app.exec()
