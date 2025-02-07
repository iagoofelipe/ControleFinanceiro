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
    [1, 'iago', 'descrição iago'],
    [2, 'iago', 'descrição iago'],
    [5, 'iago', 'descrição iago'],
    [4, 'iago', 'descrição iago'],
    [3, 'iago', 'descrição iago'],
]

ui.tableWidget.clear()
ui.tableWidget.setRowCount(len(values))
ui.tableWidget.setColumnCount(len(values[0]))

for index_row, row in enumerate(values):
    for index_col, v in enumerate(row):
        item = QTableWidgetItem(str(v))
        ui.tableWidget.setItem(index_row, index_col, item)


window.show()
app.exec()