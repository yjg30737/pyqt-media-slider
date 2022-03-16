from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt, pyqtSignal

from pyqt_resource_helper.pyqtResourceHelper import PyQtResourceHelper


class MusicSlider(QSlider):
    seeked = pyqtSignal(int)
    updatePosition = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.__pressed = None
        self.__initUi()

    def __initUi(self):
        self.setOrientation(Qt.Horizontal)

        PyQtResourceHelper.setStyleSheet([self], ['style/slider.css'])
        self.setFixedHeight(20)

        self.setMouseTracking(True)

    def __setPositionAndGetValue(self, e):
        x = e.pos().x()
        if x >= self.maximum():
            return self.maximum()
        else:
            value = self.minimum() + (self.maximum() - self.minimum()) * x / self.width()
            if value < 0:
                value = 0
            self.setValue(value)
            return value

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.__pressed = True
            e.accept()
            value = self.__setPositionAndGetValue(e)
            self.seeked.emit(value)

    def mouseMoveEvent(self, e):
        if self.__pressed:
            e.accept()
            value = self.__setPositionAndGetValue(e)
            self.updatePosition.emit(value)
        return super().mouseMoveEvent(e)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.__pressed = False
            e.accept()
            value = self.__setPositionAndGetValue(e)
            self.seeked.emit(value)
        return super().mouseReleaseEvent(e)

    def resizeEvent(self, e):
        self.setRange(0, self.width())
        return super().resizeEvent(e)