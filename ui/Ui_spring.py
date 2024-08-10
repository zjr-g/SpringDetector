# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spring.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTabWidget, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(605, 540)
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        font.setBold(False)
        font.setStyleStrategy(QFont.PreferDefault)
        Form.setFont(font)
        Form.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.infoTab = QWidget()
        self.infoTab.setObjectName(u"infoTab")
        self.verticalLayout_2 = QVBoxLayout(self.infoTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(self.infoTab)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(True)

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.tabWidget.addTab(self.infoTab, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Spring", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<h3 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:143%; background-color:#ffffff;\"><span style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:large; font-weight:700; color:#333333;\">Spring Boot Actuator\u672a\u6388\u6743\u8bbf\u95ee\u6f0f\u6d1e\u5229\u7528</span></h3>\n"
"<p style=\" margin-top:14px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-blo"
                        "ck-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333;\">Actuator \u662f Spring Boot \u63d0\u4f9b\u7684\u670d\u52a1\u76d1\u63a7\u548c\u7ba1\u7406\u4e2d\u95f4\u4ef6\u3002\u5f53 Spring Boot \u5e94\u7528\u7a0b\u5e8f\u8fd0\u884c\u65f6\uff0c\u5b83\u4f1a\u81ea\u52a8\u5c06\u591a\u4e2a\u7aef\u70b9\u6ce8\u518c\u5230\u8def\u7531\u8fdb\u7a0b\u4e2d\u3002\u5f53\u8fd9\u4e9b\u7aef\u70b9\u5b58\u5728\u914d\u7f6e\u4e0d\u5f53\u7684\u65f6\u5019\uff0c\u5c31\u6709\u53ef\u80fd\u5bfc\u81f4\u4e00\u4e9b\u7cfb\u7edf\u4fe1\u606f\u6cc4\u9732\u3001 RCE \u7b49\u5b89\u5168\u95ee\u9898\u3002</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" "
                        "style=\" margin-top:14px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">Spring Boot 1.x\u7248\u672c\u7aef\u70b9\u5728\u6839URL\u4e0b\u6ce8\u518c</span></li></ul>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:14px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">Spring Boot 2.x\u7248\u672c\u7aef\u70b9\u79fb\u52a8\u5230/actuator/\u8def\u5f84</span></li></ul>\n"
"<p style=\" margin-top:14px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial"
                        "','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333;\">\u53c2\u8003\u5b98\u7f51\u6587\u6863\uff0c\u5176\u4e2d\u5e38\u7528\u7684\u7aef\u70b9\u529f\u80fd\u63cf\u8ff0\u5982\u4e0b\uff1a</span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333;\">Actuator \u7981\u7528\u4e86\u5927\u90e8\u5206\u7aef\u70b9\u3002\u56e0\u6b64\uff0c\u9ed8\u8ba4\u60c5\u51b5\u4e0b\u53ea\u6709 </span><span style=\" font-family:'Courier New'; font-size:16px; color:#333333; background-color:#f3f4f4;\">/health</span><span style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333;\"> \u548c </span><span style=\" font-family:'Courier New'; font-size:16px; color:#333333; background-color:#f3f4f4;\">"
                        "/info</span><span style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333;\"> \u8fd9\u4e24\u4e2a\u7aef\u70b9\u53ef\u7528\u3002</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:14px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/auditevents</span><span style=\" font-size:16px;\"> \u5217\u51fa\u4e86\u4e0e\u5b89\u5168\u5ba1\u8ba1\u76f8\u5173\u7684\u4e8b\u4ef6\uff0c\u5982\u7528\u6237\u767b\u5f55/\u6ce8\u9500\u3002\u6b64\u5916\uff0c\u8fd8\u53ef\u4ee5\u6839\u636e Principal \u6216\u7c7b\u578b\u7b49\u5b57\u6bb5\u8fdb\u884c\u8fc7\u6ee4"
                        "\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/beans</span><span style=\" font-size:16px;\"> \u8fd4\u56de </span><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">BeanFactory</span><span style=\" font-size:16px;\"> \u4e2d\u6240\u6709\u53ef\u7528\u7684 Bean\u3002\u4e0e </span><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/auditevents</span><span style=\" font-size:16px;\"> \u4e0d\u540c\uff0c\u5b83\u4e0d\u652f\u6301\u8fc7\u6ee4\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color"
                        ":#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/conditions</span><span style=\" font-size:16px;\">\uff08\u4e4b\u524d\u79f0\u4e3a </span><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/autoconfig</span><span style=\" font-size:16px;\">\uff09\u4f1a\u751f\u6210\u6709\u5173\u81ea\u52a8\u914d\u7f6e\u6761\u4ef6\u7684\u62a5\u544a\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/configprops</span><span style=\" font-size:16px;\"> \u5141\u8bb8"
                        "\u83b7\u53d6\u6240\u6709 </span><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">@ConfigurationProperties</span><span style=\" font-size:16px;\"> Bean\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/env</span><span style=\" font-size:16px;\"> \u8fd4\u56de\u5f53\u524d\u73af\u5883\u5c5e\u6027\uff08Environment Properties\uff09\uff0c\u4e5f\u53ef\u4ee5\u68c0\u7d22\u5355\u4e2a\u5c5e\u6027\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; mar"
                        "gin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/flyway</span><span style=\" font-size:16px;\"> \u63d0\u4f9b\u4e86\u6709\u5173 Flyway \u6570\u636e\u5e93\u8fc1\u79fb\u7684\u8be6\u7ec6\u4fe1\u606f\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/health</span><span style=\" font-size:16px;\"> \u6c47\u603b\u4e86\u5e94\u7528\u7684\u5065\u5eb7\u72b6\u51b5\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" m"
                        "argin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/heapdump</span><span style=\" font-size:16px;\"> \u4f1a\u6784\u5efa\u5e76\u8fd4\u56de\u5e94\u7528\u6240\u7528 JVM \u7684 </span><span style=\" font-size:16px; color:#000000;\">Heap Dump</span><span style=\" font-size:16px;\">\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/info</span><span style=\" font-size:16px;\"> \u8fd4\u56de\u4e00\u822c\u4fe1\u606f\u3002\u5b83\u53ef\u80fd\u662f\u81ea\u5b9a\u4e49\u6570\u636e\u3001\u6784\u5efa\u4fe1\u606f\u6216\u6700\u65b0\u63d0\u4ea4"
                        "\u7684\u8be6\u7ec6\u4fe1\u606f\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/liquibase</span><span style=\" font-size:16px;\"> \u7684\u884c\u4e3a\u7c7b\u4f3c\u4e8e </span><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/flyway</span><span style=\" font-size:16px;\">\uff0c\u4f46\u9488\u5bf9\u7684\u662f Liquibase\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/logfile</span><span style=\" font-size:16px;\"> \u8fd4\u56de\u666e\u901a\u5e94\u7528\u65e5\u5fd7\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/loggers</span><span style=\" font-size:16px;\"> \u80fd\u591f\u67e5\u8be2\u548c\u4fee\u6539\u5e94\u7528\u7684\u65e5\u5fd7\u7ea7\u522b\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/metrics</span><span style=\" font-size:16px;\"> \u8be6\u7ec6\u4ecb\u7ecd\u4e86\u5e94\u7528\u7684\u6307\u6807\u3002\u8fd9\u53ef\u80fd\u5305\u62ec\u901a\u7528\u6307\u6807\u548c\u81ea\u5b9a\u4e49\u6307\u6807\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/prometheus</span><span style=\" font-size:16px;\"> \u8fd4\u56de\u7684\u6307\u6807\u4e0e\u524d\u4e00\u4e2a\u7c7b\u4f3c\uff0c\u4f46\u683c\u5f0f\u5316\u540e\u53ef\u4e0e Prometheus \u670d\u52a1\u5668\u4e00\u8d77\u4f7f\u7528\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helve"
                        "tica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/scheduledtasks</span><span style=\" font-size:16px;\"> \u63d0\u4f9b\u4e86\u5e94\u7528\u4e2d\u6bcf\u4e2a\u8ba1\u5212\uff08\u5b9a\u65f6\uff09\u4efb\u52a1\u7684\u8be6\u7ec6\u4fe1\u606f\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/sessions</span><span style=\" font-size:16px;\"> \u5217\u51fa\u4e86 HTTP Session\uff0c\u524d\u63d0\u662f\u6b63\u5728\u4f7f\u7528 S"
                        "pring Session\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/shutdown</span><span style=\" font-size:16px;\"> \u53ef\u4ee5\u4f18\u96c5\u5730\u5173\u95ed\u5e94\u7528\u3002</span></li>\n"
"<li style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16px; background-color:#f3f4f4;\">/threaddump</span><span style=\" font-size:16px;\"> \u4f1a dump \u5e95\u5c42 JVM \u7684\u7ebf\u7a0b\u4fe1"
                        "\u606f\u3002</span></li></ul>\n"
"<p style=\" margin-top:14px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333;\">\u5176\u4e2d\u5f53heapdump\u3001env\u3001threaddump\u7b49\u7aef\u70b9\u5b58\u5728\u672a\u6388\u6743\u8bbf\u95ee\u65f6\uff0c\u54b1\u4eec\u53ef\u4ee5\u4ece\u4e2d\u83b7\u53d6\u5230\u670d\u52a1\u5668\u5b58\u5728\u7684\u654f\u611f\u4fe1\u606f\uff0c\u5305\u62ecOSS\u79d8\u94a5\u3001\u6570\u636e\u5e93\u8fde\u63a5\u5bc6\u7801\u3001redis\u8fde\u63a5\u5bc6\u7801\u3001\u914d\u7f6e\u73af\u5883\u7b49\uff0c\u5bfc\u81f4\u7cfb\u7edf\u4fe1\u606f\u6cc4\u9732\u751a\u81f3\u4e22\u5931\u6743\u9650\u3002</span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Open Sans',"
                        "'Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333;\">fofa\u67e5\u8be2\u8bed\u6cd5:</span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Consolas','Monaco','Andale Mono','Ubuntu Mono','monospace'; font-size:14px; color:#000000; background-color:#f5f2f0;\">icon_hash</span><span style=\" font-family:'Consolas','Monaco','Andale Mono','Ubuntu Mono','monospace'; font-size:14px; color:#9a6e3a; background-color:rgba(255,255,255,0.494118);\">=</span><span style=\" font-family:'Consolas','Monaco','Andale Mono','Ubuntu Mono','monospace'; font-size:14px; color:#669900; background-color:#f5f2f0;\">&quot;116323821&quot;</span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Consolas','Monaco',"
                        "'Andale Mono','Ubuntu Mono','monospace'; font-size:14px; color:#000000; background-color:#f5f2f0;\">body</span><span style=\" font-family:'Consolas','Monaco','Andale Mono','Ubuntu Mono','monospace'; font-size:14px; color:#9a6e3a; background-color:rgba(255,255,255,0.494118);\">=</span><span style=\" font-family:'Consolas','Monaco','Andale Mono','Ubuntu Mono','monospace'; font-size:14px; color:#669900; background-color:#f5f2f0;\">&quot;Whitelabel Error Page&quot;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Consolas','Monaco','Andale Mono','Ubuntu Mono','monospace'; font-size:14px; color:#669900;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI';\">\u652f\u6301\u68c0\u6d4b\u7684\u6f0f\u6d1e\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0"
                        "px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI';\">2023 JeeSpringCloud \u4efb\u610f\u6587\u4ef6\u4e0a\u4f20\u6f0f\u6d1e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI';\">CVE-2022-22947 (Spring Cloud Gateway SpELRCE\u6f0f\u6d1e)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI';\">CVE-2022-22963 (Spring Cloud Function SpEL RCE\u6f0f\u6d1e)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI';\">CVE-2022-22965 (Spring Core RCE\u6f0f\u6d1e)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-bl"
                        "ock-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI';\">CVE-2021-21234 (\u4efb\u610f\u6587\u4ef6\u8bfb\u53d6\u6f0f\u6d1e)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI';\">2021 SnakeYAML_RCE \u6f0f\u6d1e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI';\">2021 Eureka_Xstream \u53cd\u5e8f\u5217\u5316\u6f0f\u6d1e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI';\">2020 Jolokia\u914d\u7f6e\u4e0d\u5f53\u5bfc\u81f4RCE\u6f0f\u6d1e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-famil"
                        "y:'Microsoft YaHei UI';\">CVE-2018-1273\uff08Spring Data Commons RCE\u6f0f\u6d1e\uff09</span></p>\n"
"<p style=\" margin-top:14px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'Open Sans','Clear Sans','Helvetica Neue','Helvetica','Arial','Segoe UI Emoji','sans-serif'; font-size:16px; color:#333333;\">\u53c2\u8003\u94fe\u63a5\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://blog.zgsec.cn/archives/129.html\"><span style=\" font-family:'Microsoft YaHei UI'; text-decoration: underline; color:#0000ff;\">\u5bf9\u4e8eSpring Boot\u7684\u6e17\u900f\u59ff\u52bf - AabyssZG's Blog (zgsec.cn)</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://mp.weixin.qq.com/s/pRwLkFSlVcev7srsMPRuqQ\"><span style=\" font-fam"
                        "ily:'Microsoft YaHei UI'; text-decoration: underline; color:#0000ff;\">\u3010\u5907\u5fd8\u5f55\u3011\u5e38\u7528Springboot\u6f0f\u6d1e\u5229\u7528\u59ff\u52bf\u603b\u7ed3 (qq.com)</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/hongyan454/SpringBootVulExploit?tab=readme-ov-file#%E9%9B%B6%E8%B7%AF%E7%94%B1%E5%92%8C%E7%89%88%E6%9C%AC\"><span style=\" font-family:'Microsoft YaHei UI'; text-decoration: underline; color:#0000ff;\">hongyan454/SpringBootVulExploit: SpringBoot \u76f8\u5173\u6f0f\u6d1e\u5b66\u4e60\u8d44\u6599\uff0c\u5229\u7528\u65b9\u6cd5\u548c\u6280\u5de7\u5408\u96c6\uff0c\u9ed1\u76d2\u5b89\u5168\u8bc4\u4f30 check list (github.com)</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.infoTab), QCoreApplication.translate("Form", u"SpringBootInfo", None))
    # retranslateUi

