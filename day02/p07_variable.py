# file: p07_variable.py
# desc: 변수에 대하여
from copy import copy

z = 1
print(id(z))            # id는 z가 가리키고 있는 메모리 주소를 출력해준다.

a = [1, 2, 3]
print("a", id(a))       # 1602804830592

b = a
print("b", id(b))       # 1602804830592

# del b[2]
# print(a)                # b에서 인덱스 2에 저장되어 있는 값을 삭제했는데 a의 인덱스도 함께 삭제됨(Python의 문제점)

d = copy(a)            
print("d", id(d))       # 2393961976192 -> copy를 함으로써 a와 값은 같지만 다른 메모리 주소를 가짐

del d[2]    
print(a)                # d의 2번째 인덱스에 있는 값을 삭제했지만, a는 바뀌지 않는 것을 확인할 수 있음

# c = 1
# d = 1
# print("c", id(c))       # 140730368543160
# print("d", id(d))       # 140730368543160
