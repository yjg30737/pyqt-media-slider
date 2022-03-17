# pyqt-music-slider
This is QSlider which supports the smoothly draggable handle, direct handle placement to click position for media(audio, video).

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-music-slider.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a>

## Signal
* ```pressed(int)``` Signal emit when presses the handle
* ```released(int)``` Signal emit when releases the handle

## Example
```python
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication

from pyqt_music_slider.musicSlider import MusicSlider


class MusicSliderExample(QWidget):

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__slider = MusicSlider()
        lay = QHBoxLayout()
        lay.addWidget(self.__slider)
        self.setLayout(lay)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    player = MusicSliderExample()
    player.show()
    app.exec_()
```

Result

https://user-images.githubusercontent.com/55078043/151730656-42ecb8e1-3987-415c-bc5f-8ae1d10bf2e6.mp4






