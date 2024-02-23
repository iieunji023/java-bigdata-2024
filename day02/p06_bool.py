# file: p06_bool.py
# desc: 불타입(True/False), None 타입 학습

# 참/거짓

a = True
b = False

print(a)                # True
print(type(a))          # <class 'bool'>
print(type(1))          # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type('hi'))       # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
print(type((1, 2, 3)))  # <class 'tuple'>

print(a == b)           # False
print(a != b)           # True
print(a == (not b))     # True => (not b) = True

print(bool(''))          # false = 0, 0 이외의 값은 모두 True

# 참/거짓 구분: 빈값, 0, None은 모두 False, 그 외는 True이다.

#None 타입
None

c = None
a = 1
b = 0
print(c)                # None
print(a + b)            # a = 1(True), b = 0(False) 따라서, 1 + 0 = 1
print(c + a)            # None은 값을 더할 수 없다. 아무런 값도 없기 때문