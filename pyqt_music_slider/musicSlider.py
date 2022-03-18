from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt, pyqtSignal

from pyqt_resource_helper.pyqtResourceHelper import PyQtResourceHelper


class MusicSlider(QSlider):
    pressed = pyqtSignal(int)
    dragged = pyqtSignal(int)
    released = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.__pressed = False
        self.__initUi()

    def __initUi(self):
        self.setOrientation(Qt.Horizontal)

        PyQtResourceHelper.setStyleSheet([self], ['style/slider.css'])
        self.setFixedHeight(20)

        self.setMouseTracking(True)

    def __setPositionAndGetValue(self, e):
        x = e.pos().x()

        if x > self.width() / 2:
            x += min(3, (x - self.width() / 2) / (self.width() / 2 / 3))
        elif self.width() / 2 > x > 0:
            x -= min(3, self.width() / 2 / x)

        value = self.minimum() + (self.maximum() - self.minimum()) * x / self.width()
        if value < 0:
            value = 0
        elif value >= self.maximum():
            value = self.maximum()
        self.setValue(value)
        return value

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.__pressed = True
            e.accept()
            value = self.__setPositionAndGetValue(e)
            self.pressed.emit(value)

    def mouseMoveEvent(self, e):
        if self.__pressed:
            e.accept()
            value = self.__setPositionAndGetValue(e)
            self.dragged.emit(value)
        return super().mouseMoveEvent(e)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.__pressed = False
            e.accept()
            value = self.__setPositionAndGetValue(e)
            self.released.emit(value)
        return super().mouseReleaseEvent(e)