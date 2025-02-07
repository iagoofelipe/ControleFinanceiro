# pyside6-uic financeiroapp\ui\src\Table.ui -o tests\table\ui_table.py

from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import Qt
from ui_table import Ui_Table

app = QApplication()
window = QMainWindow()
ui = Ui_Table()
wid = QWidget()

QGuiApplication.styleHints().setColorScheme(Qt.ColorScheme.Light)
ui.setupUi(wid)
window.setCentralWidget(wid)
ui.verticalLayout.setContentsMargins(10, 10, 10, 10)

values = [
    [11.4, 'iago', 'produto 1'],
    [22.4, 'iago', 'produto 2'],
    [5.5, 'marcos', 'produto 3'],
    [4.1, 'carlos', 'produto 4'],
    [3, 'carlos', 'produto 5'],
    [3, 'josé', 'produto 5'],
    [3.4, 'iago', 'produto 6'],
    [3.9, 'marcos', 'produto 7'],
]

headers = ['valor', 'atendente', 'produto']
len_headers = len(headers)

ui.tableWidget.clear()
ui.tableWidget.setColumnCount(len_headers)
ui.tableWidget.setRowCount(len(values))

for index_row, row in enumerate(values):
    
    for index_col, v in enumerate(row):
        if index_col >= len_headers:
            raise IndexError('a quantidade de valores é maior que a quantidade de colunas')
        
        item = QTableWidgetItem(str(v))
        ui.tableWidget.setItem(index_row, index_col, item)

ui.tableWidget.setHorizontalHeaderLabels(headers)
window.show()
app.exec()