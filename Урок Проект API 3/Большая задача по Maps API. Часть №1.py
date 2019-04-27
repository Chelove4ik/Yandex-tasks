import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 450)

        self.hbox = QHBoxLayout(self)
        self.setLayout(self.hbox)
        self.lbl = QLabel(self)

        name = 'res.jpg'
        pixmap = QPixmap(name)
        self.lbl.setPixmap(pixmap)
        self.hbox.addWidget(self.lbl)

        self.move(100, 200)


if __name__ == '__main__':
    response = requests.get(
        'https://static-maps.yandex.ru/1.x/?ll=131.951912,43.127849&z=11&l=sat')

    with open('res.jpg', mode='wb') as f:
        f.write(response.content)

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
