# pyqt-music-slider
This is QSlider which supports the smoothly draggable handle for media(audio, video).

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-music-slider.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a>

## Note
I'm still working because there is a couple of flaws like inaccurate placement of handle.
Sorry about that.

## Example
```python
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication

from pyqt_music_slider.musicSlider import MusicSlider


class MusicPlayer(QWidget):
    played = pyqtSignal(bool)

    def __init__(self, slider=None):
        super().__init__()
        self.__initUi(slider)

    def __initUi(self, slider=None):
        self.__slider = slider if slider else MusicSlider()
        self.__slider.updatePosition.connect(self.updatePosition) # updatePosition signal will emit when handle is moved

        lay = QHBoxLayout()
        lay.addWidget(self.__slider)

        self.setLayout(lay)

    def updatePosition(self, pos):
        print(pos) # show position of the handle while moving it


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/146923399-728d4bb7-7683-442c-8056-66c9d52bee2e.png)


