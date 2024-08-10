# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vuldetect.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(726, 578)
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.urlPlainTextEdit = QPlainTextEdit(Form)
        self.urlPlainTextEdit.setObjectName(u"urlPlainTextEdit")

        self.verticalLayout.addWidget(self.urlPlainTextEdit)

        self.loadUrlPushButton = QPushButton(Form)
        self.loadUrlPushButton.setObjectName(u"loadUrlPushButton")

        self.verticalLayout.addWidget(self.loadUrlPushButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.agencyCheckBox = QCheckBox(Form)
        self.agencyCheckBox.setObjectName(u"agencyCheckBox")
        self.agencyCheckBox.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.agencyCheckBox)

        self.detectPushButton = QPushButton(Form)
        self.detectPushButton.setObjectName(u"detectPushButton")

        self.horizontalLayout.addWidget(self.detectPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout.addLayout(self.gridLayout)

        self.logPlainTextEdit = QPlainTextEdit(Form)
        self.logPlainTextEdit.setObjectName(u"logPlainTextEdit")

        self.verticalLayout.addWidget(self.logPlainTextEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"VulDetect", None))
        self.urlPlainTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"url list", None))
        self.loadUrlPushButton.setText(QCoreApplication.translate("Form", u"LoadUrl", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"ALL", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"JeeSpringCloud_2023", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"CVE_2022_22978", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"CVE_2022_22947", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"CVE_2022_22963", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"CVE_2022_22965", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Form", u"CVE_2021_21234", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Form", u"SnakeYAML_2021_rce", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Form", u"Eureka_Xstream_2021_rce", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Form", u"Jolokia_2020_rce", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Form", u"CVE_2018_1273", None))

        self.agencyCheckBox.setText(QCoreApplication.translate("Form", u"Agency", None))
        self.detectPushButton.setText(QCoreApplication.translate("Form", u"Detect", None))
    # retranslateUi

