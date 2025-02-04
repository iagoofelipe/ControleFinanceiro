# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_Table(object):
    def setupUi(self, Table):
        if not Table.objectName():
            Table.setObjectName(u"Table")
        Table.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Table)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widHeader = QWidget(Table)
        self.widHeader.setObjectName(u"widHeader")
        self.widHeader.setStyleSheet(u"QPushButton { background-color: transparent }")
        self.horizontalLayout = QHBoxLayout(self.widHeader)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTitle = QLabel(self.widHeader)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setPointSize(13)
        self.labelTitle.setFont(font)

        self.horizontalLayout.addWidget(self.labelTitle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnConfirm = QPushButton(self.widHeader)
        self.btnConfirm.setObjectName(u"btnConfirm")
        icon = QIcon()
        icon.addFile(u":/root/Assets/check-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnConfirm.setIcon(icon)
        self.btnConfirm.setFlat(True)

        self.horizontalLayout.addWidget(self.btnConfirm)

        self.btnEdit = QPushButton(self.widHeader)
        self.btnEdit.setObjectName(u"btnEdit")
        icon1 = QIcon()
        icon1.addFile(u":/root/Assets/pen-to-square-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEdit.setIcon(icon1)
        self.btnEdit.setFlat(True)

        self.horizontalLayout.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(self.widHeader)
        self.btnDelete.setObjectName(u"btnDelete")
        icon2 = QIcon()
        icon2.addFile(u":/root/Assets/trash-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDelete.setIcon(icon2)
        self.btnDelete.setFlat(True)

        self.horizontalLayout.addWidget(self.btnDelete)


        self.verticalLayout.addWidget(self.widHeader)

        self.line = QFrame(Table)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.tableView = QTableView(Table)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(Table)

        QMetaObject.connectSlotsByName(Table)
    # setupUi

    def retranslateUi(self, Table):
        Table.setWindowTitle(QCoreApplication.translate("Table", u"Form", None))
        self.labelTitle.setText(QCoreApplication.translate("Table", u"-TITLE-", None))
        self.btnEdit.setText("")
    # retranslateUi

