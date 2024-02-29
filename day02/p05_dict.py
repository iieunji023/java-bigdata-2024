# file: p05_dict.py
# desc: 딕셔너리 자료형 학습

spiderMan = {'name': 'Peter Parker', 
             'age': 18, 
             'weapon': 'Web Shooter', 
             'friends': ['ironMan', 'Thor', 'Captain America']}

## 출력
print(spiderMan)
print(spiderMan['friends'])     # friends라는 key로 해당 키의 값만 출력할 수 있다.

## 값 추가
spiderMan['job'] = 'CameraMan'
print(spiderMan)

## 값 삭제
del spiderMan['friends']
print(spiderMan)

## 딕셔너리 함수
print(spiderMan.keys())         # 딕셔너리에 현재 존재하는 키 목록: spiderMan에 저장되어 있는 Key를 볼 수 있다.
print(list(spiderMan.keys()))   # Key 목록을 리스트 형태로 형변환
print(spiderMan.items())        # 딕셔너리의 모든 아이템 출력: 저장되어 있는 Key, Value를 볼 수 있다.
print(spiderMan.get('name'))    # 딕셔너리의 값 가져오기: Key로 Value 얻기 - get
print('friends' in spiderMan)   # 딕셔너리 안에 키가 있는지 확인(true, false로 반환): 해당 Key가 딕셔너리 안에 있는지 조사하기 - in
print(spiderMan.values())       # spiderMan에 저장되어 있는 Value를 볼 수 있다.

res = spiderMan.pop('job')      # 지정한 Key 값을 꺼내기
print(res)
print(spiderMan)                # job이 사라진 것을 볼 수 있다.

## 완전 삭제
spiderMan.clear()               # 객체까지 삭제되는 것은 X -> 출력시  {} 형태로 Key, Value가 비워져서 나옴
print(spiderMan)                

del spiderMan                   # 완전 삭제 - spiderMan 객체를 아예 지워버림
print(spiderMan)


# 집합: 중복허용X, 순서 X
# set([1, 2, 3, 4, 3, 4, 2, 1]) => 결과: {1, 2, 3, 4} , {3, 4, 1, 2}.. 등 순서가 계속 바뀌어서 출력됨