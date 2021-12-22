# pyqt-music-slider
This is QSlider which supports the smoothly draggable handle, direct handle placement to click position for media(audio, video).

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-music-slider.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a>

## Signal
* seeked(int) -> Signal emit when press or release the handle
* updatePosition(int) -> Signal emit when move the handle

## Example
```python
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication

from pyqt_music_slider.musicSlider import MusicSlider


class MusicSliderExample(QWidget):

    def __init__(self):
        super().__init__()
        self.__initUi(slider)

    def __initUi(self):
        self.__slider = MusicSlider()
        self.__slider.updatePosition.connect(self.updatePosition)

        lay = QHBoxLayout()
        lay.addWidget(self.__slider)

        self.setLayout(lay)

    def updatePosition(self, pos):
        print(pos)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    player = MusicSliderExample()
    player.show()
    app.exec_()
```

Result

https://user-images.githubusercontent.com/55078043/147012126-a0f6cc68-8403-4c61-97f6-e1931395f722.mp4




