# file: p21_review.py
# desc: p.188

f1 = open('./day03/test.txt',  mode='w', encoding='utf-8')
f1.write('Life is too short \n you need java')
f1.close()


## readlines() 썼을 때
f = open('./day03/test.txt', mode='r', encoding='utf-8')
body = f.readlines()        # 결과 리스트로 리턴
f.close()
print(body)

body = [body[0], body[1].replace('java', 'python')]
print(body)
f = open('./day03/test.txt', mode='w', encoding='utf-8')
f.write(body[0] + body[1])
f.close()

## read() 썼을 때 -  read()는 길이 제한이 있음
f = open('./day03/test.txt', mode='r', encoding='utf-8')
body = f.read()             # 문자열로 리턴. 단, read()는 text가 길면 문장이 잘려서 나온다
f.close()

body = body.replace('java', 'python')
f = open('./day03/test.txt', mode='r', encoding='utf-8')
f.write(body)
f.close()