import sys

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 450)

        self.hbox = QHBoxLayout(self)
        self.setLayout(self.hbox)
        self.lbl = QLabel(self)
        self.scale = 11
        self.coords = ['131', '43']

        self.show_img()

        self.move(100, 200)

    def show_img(self):
        response = requests.get(
            f'https://static-maps.yandex.ru/1.x/?ll={",".join(self.coords)}&z={self.scale}&l=sat')

        with open('res.jpg', mode='wb') as f:
            f.write(response.content)
        if self.lbl is not None:
            self.hbox.removeWidget(self.lbl)
        name = 'res.jpg'
        pixmap = QPixmap(name)
        self.lbl.setPixmap(pixmap)
        self.hbox.addWidget(self.lbl)

    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key_PageUp:
            if self.scale < 13:
                self.scale += 1
        if e.key() == Qt.Key_PageDown:
            if self.scale > 1:
                self.scale -= 1
        pass
        self.show_img()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
