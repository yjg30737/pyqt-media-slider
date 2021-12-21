from setuptools import setup, find_packages

setup(
    name='pyqt-music-slider',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_music_slider.style': ['slider.css']},
    description='PyQt music slider',
    url='https://github.com/yjg30737/pyqt-music-slider.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
    ]
)