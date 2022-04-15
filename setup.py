from setuptools import setup, find_packages

setup(
    name='pyqt-media-slider',
    version='0.2.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_media_slider.style': ['slider.css']},
    description='PyQt media slider',
    url='https://github.com/yjg30737/pyqt-media-slider.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
    ]
)