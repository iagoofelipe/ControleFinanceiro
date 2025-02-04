# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegistryPage.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_RegistryPage(object):
    def setupUi(self, RegistryPage):
        if not RegistryPage.objectName():
            RegistryPage.setObjectName(u"RegistryPage")
        RegistryPage.resize(1045, 759)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        RegistryPage.setFont(font)
        self.gridLayout_3 = QGridLayout(RegistryPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(RegistryPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Raised)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1045, 759))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widHistorico = QFrame(self.scrollAreaWidgetContents)
        self.widHistorico.setObjectName(u"widHistorico")
        self.widHistorico.setFrameShape(QFrame.StyledPanel)
        self.widHistorico.setFrameShadow(QFrame.Raised)
        self.historicoLayout = QVBoxLayout(self.widHistorico)
        self.historicoLayout.setSpacing(10)
        self.historicoLayout.setObjectName(u"historicoLayout")
        self.historicoLayout.setContentsMargins(15, 15, 15, 15)
        self.widHistoricoTable = QFrame(self.widHistorico)
        self.widHistoricoTable.setObjectName(u"widHistoricoTable")
        self.widHistoricoTable.setFrameShape(QFrame.StyledPanel)
        self.widHistoricoTable.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.widHistoricoTable)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 130, 341, 81))

        self.historicoLayout.addWidget(self.widHistoricoTable)


        self.gridLayout_2.addWidget(self.widHistorico, 2, 0, 1, 2)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setFont(font)

        self.verticalLayout.addWidget(self.label_8)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.frame_4)


        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_2, 5, 1, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimum(1.000000000000000)
        self.doubleSpinBox.setMaximum(999999999.990000009536743)

        self.gridLayout.addWidget(self.doubleSpinBox, 4, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.widget, 2, 0, 1, 2)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)

        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 9, 0, 1, 1)

        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox, 9, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 7, 1, 1, 1)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 6, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.frame)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateTimeEdit, 8, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(RegistryPage)

        QMetaObject.connectSlotsByName(RegistryPage)
    # setupUi

    def retranslateUi(self, RegistryPage):
        RegistryPage.setWindowTitle(QCoreApplication.translate("RegistryPage", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("RegistryPage", u"Registos Tabela", None))
        self.label_8.setText(QCoreApplication.translate("RegistryPage", u"Registros Agendados", None))
        self.label_5.setText(QCoreApplication.translate("RegistryPage", u"Conta Banc\u00e1ria", None))
        self.label.setText(QCoreApplication.translate("RegistryPage", u"Cadastre Registros", None))
        self.doubleSpinBox.setPrefix(QCoreApplication.translate("RegistryPage", u"R$ ", None))
        self.label_3.setText(QCoreApplication.translate("RegistryPage", u"Valor", None))
        self.label_2.setText(QCoreApplication.translate("RegistryPage", u"T\u00edtulo", None))
        self.radioButton.setText(QCoreApplication.translate("RegistryPage", u"Entrada", None))
        self.radioButton_2.setText(QCoreApplication.translate("RegistryPage", u"Sa\u00edda", None))
        self.label_7.setText(QCoreApplication.translate("RegistryPage", u"Data/Hora", None))
        self.label_6.setText(QCoreApplication.translate("RegistryPage", u"Cart\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(QCoreApplication.translate("RegistryPage", u"Ao ativar a recorr\u00eancia, o registro ser\u00e1 agendado para ocorrer a cada N dias. \u00c9 poss\u00edvel visualiz\u00e1-los na tabela Registros Agendados", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(QCoreApplication.translate("RegistryPage", u"Ativar recorr\u00eancia", None))
#if QT_CONFIG(tooltip)
        self.spinBox.setToolTip(QCoreApplication.translate("RegistryPage", u"intervalo de recorr\u00eancia em dias", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox.setSuffix(QCoreApplication.translate("RegistryPage", u" dia(s)", None))
        self.label_4.setText(QCoreApplication.translate("RegistryPage", u"Descri\u00e7\u00e3o", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("RegistryPage", u"HH:mm dd/MM/yyyy", None))
    # retranslateUi

