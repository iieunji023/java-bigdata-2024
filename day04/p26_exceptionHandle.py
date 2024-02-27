# file: p26_exceptionHandle.py
# desc: 예외처리
# 오류(Error): 코드상 빨간색(노란색) 밑줄이 그어지는 것
# 예외(Exception): 프로그램 실행 중에 생기는 오류(비정상적 종료)

# 1. 파일읽어서
try:
    f = open('./sanple.txt', mode='r', encoding='utf-8')   # 오류파일 열기
    res = f.readline
    print(res)
except:
    print('파일 오픈 예외 발생')
else:   # 오류가 없는 경우만 수행
    f.close()

# 2. 계산결과
try:
    print(5 / 1)
except ZeroDivisionError as e:
    print('나누기 예외 발생', e.args)
finally:
    f.close()

# a, b = 5, 3

# if a > b
#     print(True)