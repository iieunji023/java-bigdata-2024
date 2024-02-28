# file: p37_qtApp.py
# desc: PyQt5 앱 만들기
'''
PyQt5 -> Qt를 Python에서 쓸 수 있도록 만든 라이브러리
Qt -> C, C++에서 사용할 수 있는 GUI(WinApp) 프레임워크(멀티플랫폼)

설치 > pip install PyQt5
시그널 == 이벤트, 
위젯 == 컨트롤
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import *

class qtApp(QWidget):   # QWidget이 가지고 있는 속성, 변수, 함수를 모두 사용가능
    def __init__(self) -> None: 
        super().__init__()  # 생성자, 부모클래스의 생성자 함수도 실행되어야
        self.initUI()

    def initUI(self):
        self.setGeometry((1920-300)// 2, (1080-300)//2, 320, 230)    # 바탕화면 정해진 위치에 높이와 너비를 얼마나 그릴지 설정한 것
        self.setWindowTitle('세번째 qt앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 화면 UI에서 추가/변경할 것
        btn1= QPushButton('클릭', self)
        btn1.setGeometry(210,180,100,40)
        btn1.clicked.connect(self.btn1Clicked)   # 버튼클릭 시그널이 발생하면 이를 처리하는 함수 연결

        self.show() # 윈도우 창을 그리기 위한 것
    
    def btn1Clicked(self):
        QMessageBox.about(self, '버튼클릭','버튼을 눌렀습니다.')

    def closeEvent(self, QCloseEvent) -> None:  # 오버라이드(재정의)
        re = QMessageBox.question(self, '종료확인', '정말 닫으시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()    # 닫기
        else:
            QCloseEvent.ignore()    # 무시



app = QApplication(sys.argv)    # 
inst = qtApp() # 객체 생성
app.exec_() # 실제 실행