# file: p29_builtinFunc.py
# desc: 내장함수

## abs(olute) 절대값
print(abs(-5))

## all 현재 컬렉션 데이터의 조건, 값이 참인 값만 있는지 확인
print(all([1, 2, 3, 4, 0]))
print(all([1, 2, 3, (4 < 2), 5]))

## chr() 아스키나 유니코드 값을 받아서 글자로 변경
print(chr(97))
print(chr(44032))

## ascii() 영문자, 문자를 아스키숫자와 유니코드숫자로 변경
print(ascii('가'))

## dir() 객체가 지닌 변수, 함수를 알려주는 함수
print(dir(list()))
a = [1, 2]
a.append(3)
print(a)
print(dir(dict()))

## divmod() 나누기의 몫, 나머지를 한번에 구해주는 함수 
print(divmod(7, 2))     # (3, 1) - (몫, 나머지) 순의 튜플 형태로 나옴

## ⭐enumerate() : 열거하다 뜻
for i in ['Hello', 'World', 'Python']:
    print(i)

for i in enumerate(['Hello', 'World', 'Python']):
    print(i)    # 인덱스, 값 형태로 나옴

for i, data in enumerate(['Hello', 'World', 'Python']):
    print(f'{i}번째 값은 {data}입니다.')

## eval(uate) : 실행함수 
print(eval('divmod(10, 3)'))

## hex : 10진수를 16진수로
print(hex(255).upper())     # 0xff

## ⭐map : 여러 값을 한꺼번에 같은 조건으로 변경할 때
def ttime(x):
    return x * 2

print(list(map(ttime, [1,3,5,7,9])))            # map을 써서 반복데이터를 ttime() 함수로 처리하라
print(list(map(int, [1.0,2.0,3.0,4.4,])))       # map을 써서 반복데이터를 int로 바꿔라

## max()
print(max([3,9,99]))
print(max(3,9,99))

## oct() 8진수
print(oct(34))  

## ord() == ascii
print(ord('A'))
print(ord('가'))

## round() 반올림(이상징후 4.5도 4도 나옴)
print(round(4.51))
print(round(4.45, 1))

## sum() 반복되는 컬렉션 자료
print(sum([1,2,3,4,5]))
print(sum(range(1,101)))

## tuple() 다른 컬렉션을 튜플 자료형으로 변경
print(tuple([1,2,3,4,5]))

## ⭐type() 변수, 데이터 타입 리턴
print(type('Hello'))    # <class 'str'>
aa = [1,2,3,4]
print(type(aa))         # <class 'list'>

## zip() 동일한 개수로 데이터를 묶어서 리턴
## 둘의 개수가 일치하지 않으면 일치하는 것까지만 묶어주고, 나머지 값은 날라감
odd = [1,3,5,7,9]
even = [2,4,6,8,10]

total = list(zip(odd, even))        
print(total)