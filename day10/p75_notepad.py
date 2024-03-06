# file: p75_notepad.py
# desc: PyQt 메모장 만들기

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('C:/Source/java-bigdata-2024/day10/Hello PyQt.ui')[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)

    def openFunction(self):
        print('open!!')

    def saveFunction(self):
        print('save!!')

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()