# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainForm.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.resize(759, 652)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        MainForm.setFont(font)
        self.horizontalLayout = QHBoxLayout(MainForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frameSidebar = QFrame(MainForm)
        self.frameSidebar.setObjectName(u"frameSidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameSidebar.sizePolicy().hasHeightForWidth())
        self.frameSidebar.setSizePolicy(sizePolicy)
        self.frameSidebar.setFrameShape(QFrame.StyledPanel)
        self.frameSidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frameSidebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnSair = QPushButton(self.frameSidebar)
        self.btnSair.setObjectName(u"btnSair")

        self.verticalLayout.addWidget(self.btnSair)


        self.horizontalLayout.addWidget(self.frameSidebar)

        self.widContent = QWidget(MainForm)
        self.widContent.setObjectName(u"widContent")
        self.verticalLayout_2 = QVBoxLayout(self.widContent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelUsername = QLabel(self.widContent)
        self.labelUsername.setObjectName(u"labelUsername")

        self.verticalLayout_2.addWidget(self.labelUsername)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widContent)


        self.retranslateUi(MainForm)

        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"Form", None))
        self.btnSair.setText(QCoreApplication.translate("MainForm", u"sair", None))
        self.labelUsername.setText(QCoreApplication.translate("MainForm", u"Bem-vindo, Username!", None))
    # retranslateUi

