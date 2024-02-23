# file: p17_fileio.py
# desc: 파일 입출력 학습

# 컴퓨터에서 열면 무조건 닫아야 하는 것
# 1. 파일 open(), close() / 파이썬은 안 닫아도 크게 지장은 없음
# 2. 네트워크 통신 open(), close() 
# 3. DB open() or connect(), close()

# 언어체계 추가 ASCII(한글 cp949), 유니코드(utf-8)
# 상대경로, 절대경로
##C:/Source/java-bigdata-2024/day03/sample.txt --> 절대경로
# w는 매번 새로 파일 생성, a는 기존파일에 내용 추가
# 로그 등을 남길 땐 a로 작업해야 한다.
f = open('./day03/sample.txt', mode='w', encoding='utf-8')
# 파일쓰기 진행
f.write('안녕하세요. 파이썬.\n')        # 한줄 내리기 시 \n 붙여야 됨
f.write('모두 화이팅!!\n')
f.close()   # 파이썬에서는 f.close()가 없어도 됨. 다른 언어에서는 무조건 close() 해줘야 함