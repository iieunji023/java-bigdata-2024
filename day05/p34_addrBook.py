# file: p34_addrBook.py
# desc: 콘솔 주소록 프로그램

class Contact:  # 주소록 클래스
    def __init__(self, name, phoneNumber, eMail, addr) -> None:
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__eMail = eMail
        self.__addr = addr
    
    def __str__(self) -> str:   # <__main__.Contact object at 0x00000211F1A82090> 객체의 상태 출력 대신 사용자가 원하는 형태로 출력
        res = (f'이  름: {self.__name} \n'
               f'핸드폰: { self.__phoneNumber} \n'
               f'이메일: {self.__eMail} \n'
               f'주  소: {self.__addr}')
        return res
    
def setContact():   # 사용자 입력으로 주소록 받기 함수
    (name, phoneNumber, eMail, addr) = input('주소록 입력(이름, 핸드폰, 이메일, 주소 순[구분자 /]) >').split('/')
    name = name.strip() # 사용자 실수로 들어간 스페이스 제거
    phoneNumber = phoneNumber.strip()
    addr = addr.strip()
    print(f'"{name}", "{phoneNumber}", "{eMail}","{addr}"')

def displayMenu():
    menu = ('주소록 프로그램 \n'
            '1. 연락처 추가 \n'
            '2. 연락처 출력 \n'
            '3. 연락처 삭제 \n'
            '4. 종료 \n')
    print(menu)
    sel = int(input('메뉴입력 : '))
    return sel

def run():
    while True:
        setMenu = displayMenu()
        if setMenu == 4:
            break

if __name__ == '__main__':      # main entry
    print('프로그램 시작')
    run()   # 메인 함수 실행

print('프로그램 종료')