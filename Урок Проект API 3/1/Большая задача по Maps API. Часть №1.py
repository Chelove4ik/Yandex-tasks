import sys

from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
win = uic.loadUi("untitled.ui")  # расположение вашего файла .ui

win.show()
sys.exit(app.exec())
