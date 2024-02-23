# file: p25_review.py
# desc: p.185 ~ p.187

# 01. 홀수, 짝수 판별하기
# def is_odd(number):
#     if number % 2 == 1:
#         return True
#     else:
#         return False

# # 02. 모든 입력의 평균값 구하기
# def avg_numbers(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result/len(args)

# print(avg_numbers(1, 2))
# print(avg_numbers(1, 2, 3, 4, 5))

# # 03. 프로그램 오류 수정하기1
# input1 = int(input("첫 번째 숫자를 입력하세요:"))
# input2 = int(input("두 번째 숫자를 입력하세요:"))

# total = input1 + input2
# print("두 수의 합은 %s입니다" % total)

# # 04. 출력 결과가 다른 것은?
# print("you" "need" "python")
# print("you" + "need" + "python")
# print("you", "need", "python")
# print("".join(["you" "need" "python"]))

# 05. 프로그램 오류 수정하기2
f1 = open("./day03/test.txt", 'w')
f1.write("Life is too short")

f1 = open("./day03/test.txt", 'r')
print(f1.read())

# 06. 사용자 입력 저장하기
user_input = input("저장할 내용을 입력하세요")
f = open("./day03/test1.txt", "a", encoding="utf-8")
f.write(user_input)
f.write("\n")
f.close()