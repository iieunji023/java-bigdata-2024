# file: p09_ifCondition.py
# desc: if 제어문

haveMoney = True

if haveMoney == True:
    # indentation(들여쓰기) tab == space 4
    print('택시타고 가')
    print('부럽네')
else:
    print('걸어가~')
    print('돈도 없는게...')


money = 3000

if money >= 5000:
    print('택시타고 가')
    print('부럽네')
elif money < 5000 and money >= 2500:
    print('기사님 홈플러스 앞까지만 가주세요')
    print('집까지 걸어감')
else:
    print('걸어가~')
    print('돈도 없는게...')

a, b, c, d = 10, 5, 7, 9
print(a >= b)   # True
print(c > d)    # False
print(a >= b and c > d)     # False  => and ::: 1 and 1 = True(1) / 1 and 0 = False(0) / 0 and 1 = False(0) / 0 and 0 = False(0)
print(a >= b or c > d)      # True   => or :::  1 or 1 = True(1) / 1 or 0 = False(0) / 0 or 1 = False(0) / 0 or 0 = False(0)
print(not (a>=b))           # False

## print() end 옵션(많이 씀), sep 옵션
print(1 in [1, 3 , 5, 7, 9], end=',')       # 배열 안에 1이 있는지 확인 => True, False로 반환
print(6 in [1, 3, 5, 7, 9])

print('13579','246810',sep=',')

# 파이썬에선 조건 연산자를 잘 안씀
score = 60
print('success' if score >= 60 else 'falure')   # (score>=60) ? "success" : "falure"

