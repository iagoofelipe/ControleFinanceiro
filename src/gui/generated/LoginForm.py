# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginForm.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(737, 512)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        LoginForm.setFont(font)
        self.horizontalLayout = QHBoxLayout(LoginForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget = QWidget(LoginForm)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 0))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineUsername = QLineEdit(self.widget)
        self.lineUsername.setObjectName(u"lineUsername")

        self.verticalLayout.addWidget(self.lineUsername)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.linePassword = QLineEdit(self.widget)
        self.linePassword.setObjectName(u"linePassword")
        self.linePassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.linePassword)

        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        font2 = QFont()
        font2.setPointSize(10)
        self.checkBox.setFont(font2)

        self.verticalLayout.addWidget(self.checkBox)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        QWidget.setTabOrder(self.lineUsername, self.linePassword)
        QWidget.setTabOrder(self.linePassword, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.pushButton)

        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("LoginForm", u"Controle Financeiro", None))
        self.label.setText(QCoreApplication.translate("LoginForm", u"Usu\u00e1rio", None))
        self.label_2.setText(QCoreApplication.translate("LoginForm", u"Senha", None))
        self.checkBox.setText(QCoreApplication.translate("LoginForm", u"Lembrar de mim", None))
        self.pushButton.setText(QCoreApplication.translate("LoginForm", u"acessar", None))
    # retranslateUi

