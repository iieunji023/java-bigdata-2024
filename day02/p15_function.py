# file: p15: function.py
# desc: 함수 학습

def plus(a, b):     # 매개변수 + 리턴값 O
    res = a + b
    return res

def minus(a, b):    # 매개변수 O, 리턴값 X
    res = a-b
    print(res)

def multi():        # 매개변수 X, 리터값 O
    global a, c     # 함수 바깥에 있는 전역변수 a와 c를 사용하겠다.
    res = a * c     
    return res

def divide():
    global a, c
    print(a / c)

def power(a, b=10): #기본인수를 지정할 때는 뒤에서부터 지정. 앞에만 지정해주면 오류 발생
    res = a ** b
    return res

print('더하기')
a = 10
c = 7
result = plus(a, c)
print(result)

print('빼기')
minus(a, c)

print('곱하기')
result = multi()
print(result)

print('곱하기')
divide()

print(power(2))     # 기본인수 :: b의 값이 10으로 설정되어 있기 때문에 입력값을 주지 않아도 된다.

def plus_many(*items):       # 동적 매개변수 :: 여러 값을 더하고 싶을 때 사용
    result = 0
    for item in items:
        result += item
    
    return result

print(plus_many(1, 2))
print(plus_many(1, 2, 3))
print(plus_many(1, 2, 3, 4, 5))
print(plus_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def calculator(mode, *args):        # 동적 매개변수
    if mode == 'a':     # 더하기
        result = 0
        for i in args:
            result += i
    
    elif mode == 'n':   # 빼기
        result = args[0]
        for i in args[1:]:
            result -= i

    elif mode == 'm':   #곱하기
        result = 1
        for i in args:
            result *= i

    elif mode == 'd':   # 나누기
        result = args[0]
        for i in args[1:]:
            result /= i
    
    return result

print(calculator('a', 1, 2, 3, 4, 5))       # 15
print(calculator('n', 100, 10, 5, 5, 4))    # 76
print(calculator('m', 2, 2, 2, 2, 2))       # 32
print(calculator('d', 100, 5, 4, 5))        # 1.0

def print_kwargs(**items):      # 키워드 매개변수, 딕셔너리를 생성
    print(items)

print_kwargs(name='Peter Parker', age=18, weapon='Web Shooter')

# 리턴을 한번에 여러개(두개 이상) 리턴할 수 있음. 튜플로 리턴한다.
def calc2(a, b):
    res1 = a + b
    res2 = a - b
    res3 = a * b
    res4 = a / b

    return res1, res2, res3, res4       # Java에도 return을 여러 개 하는 기능 생김

a, b, c, d = calc2(3, 4)
print(a, b, c, d)

# print(calc2(10, 2))

# 익명함수 람다함수 :: 함수를 한줄로 나타낸 것
add = lambda a, b: a + b
print(add(5, 4))
