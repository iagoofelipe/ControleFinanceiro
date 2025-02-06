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
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

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

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioBtnEntrada = QRadioButton(self.widget)
        self.radioBtnEntrada.setObjectName(u"radioBtnEntrada")

        self.horizontalLayout.addWidget(self.radioBtnEntrada)

        self.radionBtnSaida = QRadioButton(self.widget)
        self.radionBtnSaida.setObjectName(u"radionBtnSaida")

        self.horizontalLayout.addWidget(self.radionBtnSaida)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.widget, 2, 0, 1, 2)

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
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(13)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.doubleSpinValor = QDoubleSpinBox(self.frame)
        self.doubleSpinValor.setObjectName(u"doubleSpinValor")
        self.doubleSpinValor.setMinimum(1.000000000000000)
        self.doubleSpinValor.setMaximum(999999999.990000009536743)

        self.gridLayout.addWidget(self.doubleSpinValor, 4, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.lineDescricao = QLineEdit(self.frame)
        self.lineDescricao.setObjectName(u"lineDescricao")
        self.lineDescricao.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineDescricao, 5, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.lineTitulo = QLineEdit(self.frame)
        self.lineTitulo.setObjectName(u"lineTitulo")
        self.lineTitulo.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineTitulo, 3, 1, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)

        self.comboConta = QComboBox(self.frame)
        self.comboConta.setObjectName(u"comboConta")

        self.gridLayout.addWidget(self.comboConta, 6, 1, 1, 1)

        self.cbRecorrencia = QCheckBox(self.frame)
        self.cbRecorrencia.setObjectName(u"cbRecorrencia")

        self.gridLayout.addWidget(self.cbRecorrencia, 9, 0, 1, 1)

        self.comboCartao = QComboBox(self.frame)
        self.comboCartao.setObjectName(u"comboCartao")

        self.gridLayout.addWidget(self.comboCartao, 7, 1, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)

        self.spinRecorrencia = QSpinBox(self.frame)
        self.spinRecorrencia.setObjectName(u"spinRecorrencia")
        self.spinRecorrencia.setMinimum(1)
        self.spinRecorrencia.setMaximum(100)

        self.gridLayout.addWidget(self.spinRecorrencia, 9, 1, 1, 1)

        self.dtEditDatahora = QDateTimeEdit(self.frame)
        self.dtEditDatahora.setObjectName(u"dtEditDatahora")
        self.dtEditDatahora.setMinimumDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.dtEditDatahora.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dtEditDatahora, 8, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnLimpar = QPushButton(self.widget_2)
        self.btnLimpar.setObjectName(u"btnLimpar")

        self.horizontalLayout_2.addWidget(self.btnLimpar)

        self.btnSalvar = QPushButton(self.widget_2)
        self.btnSalvar.setObjectName(u"btnSalvar")

        self.horizontalLayout_2.addWidget(self.btnSalvar)


        self.gridLayout.addWidget(self.widget_2, 10, 0, 1, 2)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.widAgendados = QFrame(self.scrollAreaWidgetContents)
        self.widAgendados.setObjectName(u"widAgendados")
        self.widAgendados.setFrameShape(QFrame.StyledPanel)
        self.widAgendados.setFrameShadow(QFrame.Raised)
        self.agendadosLayout = QVBoxLayout(self.widAgendados)
        self.agendadosLayout.setSpacing(10)
        self.agendadosLayout.setObjectName(u"agendadosLayout")
        self.agendadosLayout.setContentsMargins(15, 15, 15, 15)
        self.widAgendadosTable = QFrame(self.widAgendados)
        self.widAgendadosTable.setObjectName(u"widAgendadosTable")
        self.widAgendadosTable.setFrameShape(QFrame.StyledPanel)
        self.widAgendadosTable.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.widAgendadosTable)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 70, 341, 81))

        self.agendadosLayout.addWidget(self.widAgendadosTable)


        self.gridLayout_2.addWidget(self.widAgendados, 0, 1, 1, 1)

        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnMinimumWidth(0, 500)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(RegistryPage)

        QMetaObject.connectSlotsByName(RegistryPage)
    # setupUi

    def retranslateUi(self, RegistryPage):
        RegistryPage.setWindowTitle(QCoreApplication.translate("RegistryPage", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("RegistryPage", u"Hist\u00f3rico de Registros", None))
        self.radioBtnEntrada.setText(QCoreApplication.translate("RegistryPage", u"Entrada", None))
        self.radionBtnSaida.setText(QCoreApplication.translate("RegistryPage", u"Sa\u00edda", None))
        self.label_5.setText(QCoreApplication.translate("RegistryPage", u"Conta Banc\u00e1ria", None))
        self.label.setText(QCoreApplication.translate("RegistryPage", u"Cadastro de Registros", None))
        self.doubleSpinValor.setPrefix(QCoreApplication.translate("RegistryPage", u"R$ ", None))
        self.label_2.setText(QCoreApplication.translate("RegistryPage", u"T\u00edtulo", None))
        self.label_3.setText(QCoreApplication.translate("RegistryPage", u"Valor", None))
        self.label_7.setText(QCoreApplication.translate("RegistryPage", u"Data/Hora", None))
#if QT_CONFIG(tooltip)
        self.cbRecorrencia.setToolTip(QCoreApplication.translate("RegistryPage", u"Ao ativar a recorr\u00eancia, o registro ser\u00e1 agendado para ocorrer a cada N dias. \u00c9 poss\u00edvel visualiz\u00e1-los na tabela Registros Agendados", None))
#endif // QT_CONFIG(tooltip)
        self.cbRecorrencia.setText(QCoreApplication.translate("RegistryPage", u"Ativar recorr\u00eancia", None))
        self.label_6.setText(QCoreApplication.translate("RegistryPage", u"Cart\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.spinRecorrencia.setToolTip(QCoreApplication.translate("RegistryPage", u"intervalo de recorr\u00eancia em dias", None))
#endif // QT_CONFIG(tooltip)
        self.spinRecorrencia.setSuffix(QCoreApplication.translate("RegistryPage", u" dia(s)", None))
        self.dtEditDatahora.setDisplayFormat(QCoreApplication.translate("RegistryPage", u"HH:mm dd/MM/yyyy", None))
        self.label_4.setText(QCoreApplication.translate("RegistryPage", u"Descri\u00e7\u00e3o", None))
        self.btnLimpar.setText(QCoreApplication.translate("RegistryPage", u"limpar", None))
        self.btnSalvar.setText(QCoreApplication.translate("RegistryPage", u"salvar", None))
        self.label_10.setText(QCoreApplication.translate("RegistryPage", u"Registros Agendados", None))
    # retranslateUi

