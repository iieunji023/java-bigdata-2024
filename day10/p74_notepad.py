# file: p74_notepad.py
# desc: PyQt 메모장 만들기

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('C:/Source/java-bigdata-2024/day10/HelloPyQt.ui')[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()