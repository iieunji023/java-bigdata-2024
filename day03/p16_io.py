# file: p16_io.py
# desc: 입출력 학습

# input()함수 기본
# res = input('인사말을 적으세요>')
# print(res)

# num = input('곱할 수를 적으세요>')
# print(type(num))                    # <class 'str'>
# # input() 받는 값은 모두 문자열
# num = int(num)
# print(num * 2)
# 숫자를 입력받아서 계산 등을 할 때는 형변환을 해줘야 한다.
#num -= 10

num = int(input('숫자 입력> '))
print(num - 10)

## 여러 값 입력
# int(40.2)       # 40
# int('50')       # 50
# int(10,20,30)   # 정수로 변하지 않음. 튜플을 바로 int로 변경할 수 있는 방법이 없음

# 튜플의 괄호() 중 할당을 받는 쪽의 괄호()는 생략이 가능하다
# (a1, a2, a3) = input('합산 세 값을 입력(구분자는 space) > ').split(' ')     # tuple은 int타입으로 형변환할 수 없다.
(a1, a2, a3) = map(int, input('합산 세 값을 입력(구분자는 space) > ').split(' '))
print(a1, a2, a3)
print(a1+a2+a3)
# a1 = int(a1)
# a2 = int(a2)
# a3 = int(a3)
# sum = a1 + a2 + a3
# print(f'합계는 {sum}')