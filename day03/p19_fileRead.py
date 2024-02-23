# file: p18_fileRead.py
# desc: 텍스트 파일 읽기

f = open('./day03/CHANGELOG.md', mode='r', encoding='utf-8')

while(True):
    read = f.readline()         # 한줄씩 읽고, 더이상 읽을 게 없으면 나옴
    if not read: break          # 더이상 읽은 값이 없으면 반복문 탈출
    print(read.replace('\n', ''))

f.close()