# file: p50_mouseAuto.py
# desc: PyAutoGui로 마우스 조작하기

'''
파이썬 모듈 설치시 명령 프롬프트보다 VSCode 내 터미널에서 설치를 추천
PyAutoGui 모듈 설치
> pip install pyautogui
'''

import pyautogui as auto

print(auto.size())    # 현재 모니터 해상도 정보(width=1920, height=1080)
print(auto.position())  # 현재 마우스 커서의 위치 정보

# pyautogui mouse 설정 창
# pillow 모듈이 같이 설치되어야 색상 표시 가능
# auto.mouseInfo()

## 마우스 이동(절대좌표)
auto.moveTo(100, 51)    #(0, 0) 이후 이동이 안됨
auto.moveTo(525,51, duration=1.0)   # x축 525, y축 51로 1.0초동안 이동
auto.moveTo(1210, 568, duration=0.1)

## 마우스 이동(상대좌표)
# auto.move(500, 500, duration=1.5) # 현재 위치에서 x축 500, y축 500으로 1.5초동안 이동

## 마우스 클릭
# auto.leftClick(x=525, y=51) # 해당위치로 가서 바로 왼쪽버튼 클릭
# auto.rightClick(x=700, y=300)
auto.click(clicks=4, interval=0.1, button='left') # 왼쪽 버튼을 소스코드 에디터에서 네번 선택하면 모든 글을 전체선택

## 마우스 드래그
auto.click(x=1380, y=311, duration=1.0) # 1380, 311에서 왼쪽 마우스 클릭 후 1초 대기
auto.dragTo(x=462, y=646, duration=2.0, button='left')
# auto.dragRel(500, 400, duration=1.0, button='left') # (상대경로) 현재 위치에서 500, 400으로 1초동안 드래그

## 마우스 휠
auto.scroll(1000)   # 양수는 위로
auto.scroll(-300)   # 음수는 아래로