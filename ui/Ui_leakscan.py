# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'leakscan.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QLayout, QPlainTextEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(760, 511)
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

        self.HorizontalLayout_1 = QHBoxLayout()
        self.HorizontalLayout_1.setObjectName(u"HorizontalLayout_1")
        self.threadCountSpinBox = QSpinBox(Form)
        self.threadCountSpinBox.setObjectName(u"threadCountSpinBox")
        self.threadCountSpinBox.setMinimumSize(QSize(100, 30))
        self.threadCountSpinBox.setMinimum(1)
        self.threadCountSpinBox.setMaximum(100)
        self.threadCountSpinBox.setValue(10)

        self.HorizontalLayout_1.addWidget(self.threadCountSpinBox)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 16777215))

        self.HorizontalLayout_1.addWidget(self.label)

        self.delayDoubleSpinBox = QDoubleSpinBox(Form)
        self.delayDoubleSpinBox.setObjectName(u"delayDoubleSpinBox")

        self.HorizontalLayout_1.addWidget(self.delayDoubleSpinBox)

        self.agencyCheckBox = QCheckBox(Form)
        self.agencyCheckBox.setObjectName(u"agencyCheckBox")
        self.agencyCheckBox.setMaximumSize(QSize(100, 16777215))

        self.HorizontalLayout_1.addWidget(self.agencyCheckBox)

        self.startPushButton = QPushButton(Form)
        self.startPushButton.setObjectName(u"startPushButton")
        self.startPushButton.setEnabled(True)

        self.HorizontalLayout_1.addWidget(self.startPushButton)


        self.verticalLayout.addLayout(self.HorizontalLayout_1)

        self.logPlainTextEdit = QPlainTextEdit(Form)
        self.logPlainTextEdit.setObjectName(u"logPlainTextEdit")
        self.logPlainTextEdit.setEnabled(True)
        self.logPlainTextEdit.setUndoRedoEnabled(True)

        self.verticalLayout.addWidget(self.logPlainTextEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.scanStatusLabel = QLabel(Form)
        self.scanStatusLabel.setObjectName(u"scanStatusLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scanStatusLabel.sizePolicy().hasHeightForWidth())
        self.scanStatusLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.scanStatusLabel)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setMinimumSize(QSize(300, 20))
        self.progressBar.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_2.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"LeakScan", None))
        self.urlPlainTextEdit.setPlainText("")
        self.urlPlainTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"url list", None))
        self.loadUrlPushButton.setText(QCoreApplication.translate("Form", u"LoadUrl", None))
        self.label.setText(QCoreApplication.translate("Form", u"Delay Time:", None))
        self.agencyCheckBox.setText(QCoreApplication.translate("Form", u"Agency", None))
        self.startPushButton.setText(QCoreApplication.translate("Form", u"Start", None))
        self.scanStatusLabel.setText(QCoreApplication.translate("Form", u"No scanning", None))
    # retranslateUi

