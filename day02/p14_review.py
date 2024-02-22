# file: p14_review.py
# desc: 149 ~ 151

# 01. 조건문의 참과 거짓
a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

# 02. 3의 배수의 합 구하기
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)

# 03. 별 표시하기
i = 0
while True:
    i += 1
    if i > 5:
        break
    print("*" * i)
   

# 04. 1부터 100까지 출력하기
for i in range(1,101):
    print(i, end=', ')

print()

# 05. 평균 점수 구하기
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print("average: ", average)

# 06. 리스트 컴프리헨션 사용하기
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n * 2)
# print(result)


number = [1, 2, 3, 4, 5]
result = [num * 2 for num in number if num % 2 != 0]
print(result)