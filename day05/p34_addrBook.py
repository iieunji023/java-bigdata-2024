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
    


def run():
    first = Contact('홍길동', '010-2323-3434', 'hdg@naver.com', '경성')
    # first = Contact(addr='경성', phoneNumber='010-2222-3333', name='홍길동', eMail='hgd@naver.com')   # 생성자 매개변수 순이 아닌 원하는 순서대로 작성할 수 있다.
    print(first)

if __name__ == '__main__':      # main entry
    print('프로그램 시작')
    run()   # 메인 함수 실행

print('프로그램 종료')