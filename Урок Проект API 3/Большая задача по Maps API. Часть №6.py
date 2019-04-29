import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication, QRadioButton, QButtonGroup, QPushButton, \
    QLineEdit
from requests import get


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 200, 850, 550)

        self.hbox = QHBoxLayout(self)
        self.setLayout(self.hbox)
        self.lbl = QLabel(self)
        self.scale = 11
        self.coords = [131, 43]
        self.l = 'sat'
        self.point = '99999,99999,flag'

        self.sat = QRadioButton('Спутник', self)
        self.sat.data = 'sat'
        self.sat.setChecked(True)
        self.sat.move(650, 50)
        self.scheme = QRadioButton('Схема', self)
        self.scheme.data = 'map'
        self.scheme.move(650, 100)
        self.hybrid = QRadioButton('Гибрид', self)
        self.hybrid.data = 'sat,skl'
        self.hybrid.move(650, 150)

        self.b_group = QButtonGroup()
        self.b_group.addButton(self.sat)
        self.b_group.addButton(self.scheme)
        self.b_group.addButton(self.hybrid)
        for rb in self.b_group.buttons():
            rb.released.connect(self.set_l)

        self.find_input = QLineEdit(self)
        self.find_input.move(650, 10)

        self.btn = QPushButton('Show image', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(750, 510)
        self.btn.clicked.connect(lambda: self.show_img(True))

        self.move(100, 200)

    def show_img(self, search=False):
        if self.find_input.text() and search:
            response = get(
                f'http://geocode-maps.yandex.ru/1.x/?geocode={self.find_input.text()}&format=json').json()[
                'response']['GeoObjectCollection']['featureMember']
            self.coords = list(map(float, response[0]['GeoObject']['Point']['pos'].split()))
            self.point = f'{self.coords[0]},{self.coords[1]},pm2dom'
        response = get(
            f'https://static-maps.yandex.ru/1.x/?ll={self.coords[0]},{self.coords[1]}&z={self.scale}&l={self.l}&pt={self.point}')

        with open('res', mode='wb') as f:
            f.write(response.content)
        if self.lbl is not None:
            self.hbox.removeWidget(self.lbl)
        name = 'res'
        pixmap = QPixmap(name)
        self.lbl.setPixmap(pixmap)
        self.lbl.adjustSize()

    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key_PageUp:
            if self.scale < 19:
                self.scale += 1
        if e.key() == Qt.Key_PageDown:
            if self.scale > 1:
                self.scale -= 1
        if e.key() == Qt.Key_Up:
            self.coords[1] += 0.01 * (20 - self.scale) ** 2 / self.scale
        if e.key() == Qt.Key_Down:
            self.coords[1] -= 0.01 * (20 - self.scale) ** 2 / self.scale
        if e.key() == Qt.Key_Left:
            self.coords[0] -= 0.01 * (20 - self.scale) ** 2 / self.scale
        if e.key() == Qt.Key_Right:
            self.coords[0] += 0.01 * (20 - self.scale) ** 2 / self.scale

        self.show_img()

    def set_l(self):
        self.l = self.sender().data
        self.show_img()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
