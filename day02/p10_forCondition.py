# file: p10_forCondition.py
# desc: for 반복문

# for item in 반복할 객체:
#       ...

a = [1, 2, 3]       # 1 하나의 값만 있는 경우에는 오류 발생
print(type(a))

for i in a:
    print(type(i))

for i in ['one', 'two', 'three']:
    print(type(i))


b = [(1, 2), (3, 4), (5, 6)]    # tuple의 집합리스트

for i in b:
    print(i)

for first, second in b:        # (first, second) tuple의 괄호는 생략가능
    print(first, second)        # tuple의 왼쪽, 오른쪽 원소에 접근

# 평균 내기
grade = [90, 80, 50, 70, 10]
sum = 0

for i in grade:
    sum += i
    print("sum:", sum)              # 총합
    print("avg:", sum/len(grade))   # 평균

## range()
print(range(10))
print(range(0,10))          # 0 ~ 9

for i in range(0, 10):      # 9 + 1
    print(i, end=' ')       # 0 1 2 3 4 5 6 7 8 9 

print()
print(list(range(0, 10)))
print(list(range(0, 10, 2)))    # 0 ~ 9까지 짝수만
print(list(range(0, 10 + 1, 2)))
print(list(range(1, 10, 2)))    # 3의 배수

print(list(range(10, 0, -2)))
print(list(range(4, 101, 4)))   # 4의 배수
print(list(range(10, 0, -1)))   

res = 0
for i in range(1, 1001):
    res += i

print(res)

## list comprehension 리스트 내포
# list(range())만으로도 리스트를 생성할 수 있지만, 여러 조건으로 리스트를 생성할 때는 list comprehension을 쓰는 것이 좋다.
print([i for i in range(1, 1001)])
print(list(range(1,1001)))
print([num * 3 for num in range(1, 1001) if num % 3== 0])