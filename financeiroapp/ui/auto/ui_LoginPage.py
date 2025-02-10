# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginPage.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        if not LoginPage.objectName():
            LoginPage.setObjectName(u"LoginPage")
        LoginPage.resize(763, 399)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        LoginPage.setFont(font)
        self.gridLayout = QGridLayout(LoginPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.frame = QFrame(LoginPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(21)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.lineUsername = QLineEdit(self.frame)
        self.lineUsername.setObjectName(u"lineUsername")
        self.lineUsername.setMaxLength(45)
        self.lineUsername.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineUsername)

        self.linePassword = QLineEdit(self.frame)
        self.linePassword.setObjectName(u"linePassword")
        self.linePassword.setMaxLength(45)
        self.linePassword.setEchoMode(QLineEdit.Password)
        self.linePassword.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.linePassword)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.cbRemember = QCheckBox(self.widget)
        self.cbRemember.setObjectName(u"cbRemember")

        self.horizontalLayout.addWidget(self.cbRemember)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.widget)

        self.btnLogin = QPushButton(self.frame)
        self.btnLogin.setObjectName(u"btnLogin")

        self.verticalLayout.addWidget(self.btnLogin)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)


        self.retranslateUi(LoginPage)

        QMetaObject.connectSlotsByName(LoginPage)
    # setupUi

    def retranslateUi(self, LoginPage):
        LoginPage.setWindowTitle(QCoreApplication.translate("LoginPage", u"Form", None))
        self.label.setText(QCoreApplication.translate("LoginPage", u"Controle Financeiro", None))
        self.lineUsername.setPlaceholderText(QCoreApplication.translate("LoginPage", u"Usu\u00e1rio", None))
        self.linePassword.setPlaceholderText(QCoreApplication.translate("LoginPage", u"Senha", None))
        self.cbRemember.setText(QCoreApplication.translate("LoginPage", u"lembrar de mim", None))
        self.btnLogin.setText(QCoreApplication.translate("LoginPage", u"login", None))
    # retranslateUi

