# Q1, Q2 Q6, Q7, Q11, Q12 - datatime을 사용해서 해보기

## Q1. 클래스 상속받고 메서드 추가하기1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

## Q2. 클래스 상속받고 메서드 추가하기2

## Q6. 리스트 항목마다 3 곱하여 리턴하기
def ttime(x):
    return x * 3

print(list(map(ttime, [1,2,3,4])))

## Q7. 최댓값과 최솟값의 합
mx =  max([-8, 2, 7, 5, -3, 5, 0, 1])
mn = min([-8, 2, 7, 5, -3, 5, 0, 1])
print(mx + mn)

## Q11. 날짜 표시하기
import datetime

curr = datetime.datetime.now()
print(f'{curr.year}/{curr.month}/{curr.day} {curr.hour}:{curr.minute}:{curr.second}')
