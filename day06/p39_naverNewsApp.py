# file : p39_naverNewsApp.py
# desc : PyQt5, QtDesigner,naver API 연동 뉴스검색 앱 만들기

import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import webbrowser   # 기본 웹브라우저 모듈
from naverSearch import NaverSearch
import datetime
import time

class qtApp(QWidget):
    def __init__(self) -> None: 
        super().__init__()
        self.initUI()
       
    def initUI(self):   # ui파일을 로드해서 화면 디자인 사용
        uic.loadUi('./day06/naverNews.ui', self)    # ui 파일 맞춰서 변겅
        self.setWindowIcon(QIcon('./images/news.png'))  # 아이콘파일에 맞춰 변경
        # 버튼 시그널처리
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        self.txtSearchWord.returnPressed.connect(self.btnSearchClicked)   # 검색 버튼 시그널 함수를 연결
        self.tblSearchResult.itemSelectionChanged.connect(self.tblResultSelected)
        self.show()

    def tblResultSelected(self):    # 테이블 클릭 시 처리
        selectRow = self.tblSearchResult.currentRow()  # 현재 선택된 행의 인덱스
        url = self.tblSearchResult.item(selectRow, 1).text()
        # QMessageBox.about(self, 'popup', url)
        webbrowser.open(url)
        
    def btnSearchClicked(self): # 검색 버튼 클릭 시 처리
        searchWord = self.txtSearchWord.text().strip()  # 공백 없애기
        
        if (len(searchWord)) == 0:  # Validation Check(입력 검증)
            QMessageBox.about(self, '네이버검색', '검색어를 입력하세요.')
            return  # 함수 탈출

        # QMessageBox.about(self, '네이버검색', '검색시작')
        # 검색 시작
        api = NaverSearch() # api 객체 생성
        jsonSearch = api.getSearchResult(searchWord)
        # print(jsonSearch)
        self.makeTable(jsonSearch)   # 검색 결과로 리스트 뷰를 만드는 함수 호출

    def makeTable(self, data):
        result = data['items']  # 네이버 검색 결과의 키 items의 값들만 활용
        # print(len(result))  # 검색 결과
        # tblSearchResult 리스트뷰 작업 시작
        self.tblSearchResult.setColumnCount(3)
        self.tblSearchResult.setRowCount(len(result))   # 10면 10
        self.tblSearchResult.setHorizontalHeaderLabels(['기사제목', '뉴스링크', '게시일자'])

        n = 0
        for post in result:
            # html 태그, 특수문자 삭제를 해야 함(<b>손흥민</b>, &lt;[<], &gt;[>], &quot;['] &nbsp;[ ])
            title = str(post['title']).replace('<b>', '').replace('</b>', '').replace('&quot;', '"')
            self.tblSearchResult.setItem(n, 0, QTableWidgetItem(title))

            # self.tblSearchResult.setItem(n, 0, QTableWidgetItem(post['title']))
            self.tblSearchResult.setItem(n, 1, QTableWidgetItem(post['link']))
            # 현재날짜 Thu, 29 Feb 2024 09:00:00 +09:00 --> 2024-02-29로 변경하는 작업
            tempDates = str(post['pubDate']).split(' ')
            year = tempDates[3]
            month = time.strptime(tempDates[2], '%b').tm_mon # Feb, Mar 같은 영어 단축 이름을 2, 3 같은 월에 대한 숫자로 변경하는 로직
            month = f'{month:02d}'  # 월에 대한 두자리 만들 때 01, 02
            day = tempDates[1]
            date = f'{year}-{month}-{day}'
            self.tblSearchResult.setItem(n, 2, QTableWidgetItem(date))
            n += 1

        self.tblSearchResult.setColumnWidth(0, 430) #QTable에 가로 스크롤을 없애기 위해서
        self.tblSearchResult.setColumnWidth(1, 200) 
        self.tblSearchResult.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 컬럼 더블클릭 금지
       
    def closeEvent(self, QCloseEvent) -> None: 
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.Cancel)
        if re == QMessageBox.Yes:   # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()    # 돌아가기(취소)

app = QApplication(sys.argv)
inst = qtApp()
app.exec_()