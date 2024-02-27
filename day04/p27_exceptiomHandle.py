# file: p27_exceptiomHandle.py
# desc: 예외처리2
# 비정상적인 종료를 막기 위한 것

# while True:
#     try:
#         select = input('메뉴입력 1.저장 2.검색 3.종료 > ')
#     except:
#         print('예외발생 입력을 최대로 하세요')  

#     if select == '1':
#         print('입력')   
#     elif select == '2':
#         print('검색')   
#     elif select == '3':
#         break
#     else:
#         continue 

class chicken:
    def fly(self):
        raise NotImplementedError   #  구현을 안했다는 의미
    
koko = chicken()
try:
    koko.fly()
except Exception as e:
    print('닭은 날 수 없다', e.args)