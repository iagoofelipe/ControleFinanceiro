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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_Table(object):
    def setupUi(self, Table):
        if not Table.objectName():
            Table.setObjectName(u"Table")
        Table.resize(615, 521)
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        self.labelTitle.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(13)
        self.labelTitle.setFont(font)

        self.horizontalLayout.addWidget(self.labelTitle)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

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

        self.widget_2 = QWidget(Table)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        self.tableWidget.setFont(font1)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.horizontalLayout_2.addWidget(self.tableWidget)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget = QWidget(Table)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QPushButton { background-color: transparent; }")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnPrv = QPushButton(self.widget)
        self.btnPrv.setObjectName(u"btnPrv")
        icon3 = QIcon()
        icon3.addFile(u":/root/Assets/circle-arrow-left-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPrv.setIcon(icon3)
        self.btnPrv.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnPrv)

        self.btnNext = QPushButton(self.widget)
        self.btnNext.setObjectName(u"btnNext")
        icon4 = QIcon()
        icon4.addFile(u":/root/Assets/circle-arrow-right-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnNext.setIcon(icon4)
        self.btnNext.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnNext)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Table)

        QMetaObject.connectSlotsByName(Table)
    # setupUi

    def retranslateUi(self, Table):
        Table.setWindowTitle(QCoreApplication.translate("Table", u"Form", None))
        self.labelTitle.setText(QCoreApplication.translate("Table", u"-TITLE-", None))
        self.btnEdit.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Table", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Table", u"Coluna 2", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Table", u"New Row", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Table", u"linha 2", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Table", u"a", None));
        ___qtablewidgetitem5 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Table", u"12", None));
        ___qtablewidgetitem6 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Table", u"3", None));
        ___qtablewidgetitem7 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Table", u"a", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("Table", u"1 a 5 de 10", None))
    # retranslateUi

