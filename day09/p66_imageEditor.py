# file: p66_imageEditor.py
# desc: PyQt 이미지 에디터
'''
qrc 파일을 사용하려면
> pyrcc5 "resource.qrc" -o "resources_rc.py"
를 통해 qrc파일을 파이썬에서 사용할 수 있도록 컴파일해줌

imutils
> pip install imutils
'''
import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# 리소스 파일 추가
import resources_rc
# OpenCV, imutils 모듈 추가
import cv2, imutils

class winApp(QMainWindow):   # QWidget 아님
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self):
        # uic.loadUi('./day09/pyNewPaint.ui', self)   # VSCode 실행용
        uic.loadUi('C:/Source/java-bigdata-2024/day09/pyNewPaint.ui', self)   # PyInstaller용 절대경로를 다 적어줘야 함
        # self.setWindowIcon(QIcon('./day09/imgs/editor.png'))
        self.setWindowIcon(QIcon('C:/Source/java-bigdata-2024/day09/imgs/editor.png'))
        self.setWindowTitle('이미지에디터  v0.5')
        ## 이미지 추가 / 여러가지 UI에 대한 초기화
        # pixmap = QPixmap('./day09/ding.jpg').scaledToHeight(471)
        pixmap = QPixmap('C:/Source/java-bigdata-2024/day09/ding.jpg').scaledToHeight(471)
        self.lblCanvas.setPixmap(pixmap)
        self.brushColor = Qt.red    # 빨간색이 기본
        ## UI 초기화 끝
        self.show()

    def initSignal(self):
        # 메뉴/툴바 액션에 대한 시그널처리함수 선언...
        self.action_New.triggered.connect(self.actionNewClicked)
        self.action_Open.triggered.connect(self.actionOpenClicked)
        self.action_Save.triggered.connect(self.actionSaveClicked)
        self.action_Exit.triggered.connect(self.actionExitClicked)
        self.action_PenRed.triggered.connect(self.actionPenRedClicked)
        self.action_PenGreen.triggered.connect(self.actionPenGreenClicked)
        self.action_PenBlue.triggered.connect(self.actionPenBlueClicked)
        self.action_About.triggered.connect(self.actionAboutClicked)
        # 변환 메뉴 추가
        self.action_G.triggered.connect(self.actionGrayscaleClicked)

    def actionGrayscaleClicked(self):
        # temp.png와 같은 형태로 임시 이미지 저장
        # OpenCV로 불러옴
        # 그레이스케일로 변경한 다음
        # 변경한 이미지를 다시 pixmap으로 변환한 후 lblCanvas에 올림
        tempPath = './day09/temp.png'
        pixmap = self.lblCanvas.pixmap()    # 라벨에 있는 그림을 pixmap 변수에 저장
        pixmap.save(tempPath)
        image = cv2.imread(tempPath)
        grayImg = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_Grayscale16)
        self.lblCanvas.setPixmap(QPixmap.fromImage(grayImg))

    def actionNewClicked(self):
        canvas = QPixmap(self.lblCanvas.width(), self.lblCanvas.height())
        canvas.fill(QColor('white'))
        self.lblCanvas.setPixmap(canvas)

    def actionOpenClicked(self):
        image = QFileDialog.getOpenFileName(self, '이미지 열기', '', 'Image file(*.jpg;*.png;*.gif)') 
        imagePath = image[0]
        pixmap = QPixmap(imagePath).scaledToHeight(471)
        self.lblCanvas.setPixmap(pixmap)
        self.lblCanvas.adjustSize()
    
    def actionSaveClicked(self):
        filePath, _ = QFileDialog.getSaveFileName(self, '이미지 저장', '', 'Image file(*.jpg;*.png;*.gif)')
        if filePath == '':
            return
        pixmap = self.lblCanvas.pixmap()
        pixmap.save(filePath)

    def actionExitClicked(self):
        cv2.destroyAllWindows()
        exit(0) # 종료

    def actionPenRedClicked(self):
        self.brushColor  = Qt.red

    def actionPenGreenClicked(self):
        self.brushColor  = Qt.green

    def actionPenBlueClicked(self):
        self.brushColor  = Qt.blue

    def actionAboutClicked(self):
        QMessageBox.about(self, '알림', '이미지 에디터 v0.5')

    def mouseMoveEvent(self, e) -> None:
        print(e.x(), e.y()-70)
        brush = QPainter(self.lblCanvas.pixmap())   # lblCanvas에 브러쉬 하나 생성
        brush.setPen(QPen(self.brushColor, 3.5, style=Qt.SolidLine, cap=Qt.RoundCap))
        brush.drawPoint(e.x(), e.y()-70)
        brush.end()
        self.update()   # 화면 업데이트
    
    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:QCloseEvent.accept()
        else:QCloseEvent.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = winApp()
    sys.exit(app.exec_())