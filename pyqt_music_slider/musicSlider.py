from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt, pyqtSignal

from pyqt_resource_helper.pyqtResourceHelper import PyQtResourceHelper


class MusicSlider(QSlider):
    seeked = pyqtSignal(int)
    updatePosition = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi_initUi(self):
        self.__pressed = None

        self.setOrientation(Qt.Horizontal)

        PyQtResourceHelper.setStyleSheet([self], ['style/slider.css'])
        self.setFixedHeight(20)

        self.setMouseTracking(True)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.__pressed = True
            # todo pause slider when pressed

            e.accept()
            x = e.pos().x()
            value = self.minimum() + (self.maximum() - self.minimum()) * x / self.width()
            self.setValue(value)
            self.seeked.emit(value)
        return super().mousePressEvent(e)

    def mouseMoveEvent(self, e):
        if self.__pressed:
            e.accept()
            x = e.pos().x()
            value = self.minimum() + (self.maximum() - self.minimum()) * x / self.width()
            self.setValue(value)
            self.updatePosition.emit(value)
        return super().mouseMoveEvent(e)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.__pressed = False

            e.accept()
            x = e.pos().x()
            value = self.minimum() + (self.maximum() - self.minimum()) * x / self.width()
            self.setValue(value)
            self.seeked.emit(value)
        return super().mouseReleaseEvent(e)

