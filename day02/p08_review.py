# file: p08_review.py
# desc: 리뷰

## 2, 3, 5, 6, 10 문제 풀기(p.116~)

#01 평균 점수 구하기
a, b, c = 80, 75, 55
result = (a+b+c) / 3
print("[01]", result)

# 02. 홀수, 짝수 판별하기
# 자연수 13이 홀수인지, 짝수인지 판별할 수 있는 방법에 대해 말해보자.
a = 13
print('[02] a는', end='')
if a % 2 == 0 : 
    print("짝수")
else:
    print("홀수")

# 03. 주민등록번호 나누기
pin = "881120-1068234"
# yyyymmdd = pin[0:6];
yyyymmdd = pin.split('-')[0]
num = pin.split('-')[1]
print("[03]", yyyymmdd)
print("[03]", num)
## print("[03]",pin[-7:])

# 04. 주민등록번호 인덱싱
pin = "881120-1068234"
print("[04]",pin[7])
 
# 05. 문자열 바꾸기
a = "a:b:c:d"
b = a.replace(":","#")
print("[05]",b)

# 06. 리스트 역순 정렬하기
a = [1, 3, 5, 4, 2]
a.sort
a.sort(reverse=True)
print("[06]",a)

# 07. 리스트를 문자열로 만들기
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print("[07]", result)

# 08. 튜플 더하기
a = (1, 2, 3)
a = a + (4, )
print("[08]",a)

# 10. 딕셔너리 값 추출하기
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print("[10]",a)
print("[10]",result)

# 11. 리스트에서 중복 제거하기
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print("[11]", b)
