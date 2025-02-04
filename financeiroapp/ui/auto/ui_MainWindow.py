# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1070, 573)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.mainLayout = QHBoxLayout(MainWindow)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.frame = QFrame(MainWindow)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 172, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btnHome = QPushButton(self.frame)
        self.btnHome.setObjectName(u"btnHome")

        self.verticalLayout.addWidget(self.btnHome)

        self.btnReg = QPushButton(self.frame)
        self.btnReg.setObjectName(u"btnReg")

        self.verticalLayout.addWidget(self.btnReg)

        self.btnContaCartao = QPushButton(self.frame)
        self.btnContaCartao.setObjectName(u"btnContaCartao")

        self.verticalLayout.addWidget(self.btnContaCartao)

        self.verticalSpacer = QSpacerItem(20, 172, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.btnConfig = QPushButton(self.frame)
        self.btnConfig.setObjectName(u"btnConfig")

        self.verticalLayout.addWidget(self.btnConfig)

        self.btnLogout = QPushButton(self.frame)
        self.btnLogout.setObjectName(u"btnLogout")

        self.verticalLayout.addWidget(self.btnLogout)


        self.mainLayout.addWidget(self.frame)

        self.widContent = QWidget(MainWindow)
        self.widContent.setObjectName(u"widContent")

        self.mainLayout.addWidget(self.widContent)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"tela inicial", None))
        self.btnReg.setText(QCoreApplication.translate("MainWindow", u"registros", None))
        self.btnContaCartao.setText(QCoreApplication.translate("MainWindow", u"contas e cart\u00f5es", None))
        self.btnConfig.setText(QCoreApplication.translate("MainWindow", u"configura\u00e7\u00f5es", None))
        self.btnLogout.setText(QCoreApplication.translate("MainWindow", u"sair", None))
    # retranslateUi

