# file: p36_qtApp.py
# desc: PyQt5 앱 만들기
'''
PyQt5 -> Qt를 Python에서 쓸 수 있도록 만든 라이브러리
Qt -> C, C++에서 사용할 수 있는 GUI(WinApp) 프레임워크(멀티플랫폼)

설치 > pip install PyQt5
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
# QMainWindow, QLabel, QPushButton 등은 QWidget을 상속한 자식 클래스(부모 클래스의 능력들을 모두 사용할 수 있다.)
from PyQt5.QtWidgets import * #QApplication, QWidget, QMainWindow, QLabel

class qtApp(QWidget):   # QWidget이 가지고 있는 속성, 변수, 함수를 모두 사용가능
    def __init__(self) -> None: 
        super().__init__()  # 생성자, 부모클래스의 생성자 함수도 실행되어야
        self.initUI()

    def initUI(self):
        label = QLabel()    # 라벨위젯(qt) == 라벨컨트롤(MFC, C#, Java, Android)
        
        
        self.setGeometry(300, 300, 800, 400)    # 바탕화면 정해진 위치에 높이와 너비를 얼마나 그릴지 설정한 것
        self.setWindowTitle('두번째 qt앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        self.text = 'What a wonderful world..'
        label.setText(self.text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet(('color: red;'
                             'background-color:black;'))   # 라벨의 색상스타일 설정 html css와 완전 동일

        font = label.font()
        font.setFamily('Bauhaus 93')
        font.setPointSize(40)
        

        label.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)

        self.show() # 윈도우 창을 그리기 위한 것

    def paintEvent(self, event) -> None:
        paint = QPainter()  # 윈도창 위에 그림 그리는 객체
        paint.begin(self)   # 그림을 그리기 시작하면
        paint.setPen(QColor(200, 0, 0)) # dark red
        paint.setFont(QFont('Bauhaus 93', 40))
        paint.drawText(250, 400//2, 'Hello PyQt!')
        paint.end() # 반드시 닫아야 함

app = QApplication(sys.argv)    # 
inst = qtApp() # 객체 생성
app.exec_() # 실제 실행