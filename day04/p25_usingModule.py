# file: p25_usingModule.py
# desc: 모듈 사용

# import calc as c     # calc.py를 사용하겠다.
from calc import mul   # mul() 함수명만 쓰면 됨

from day03.p22_carClass import Car # 디렉토리(모듈묶음: 패키지).모듈명

# import Math
from Math import Math   # from Math = 모듈(파일이름) import Math = 클래스 이름

if __name__ == '__main__':      ## Java의 void main()과 동일
    # result = c.mul(10, 7)
    result = mul(10, 7)
    print("a + b =", result)

    print(__name__)     ## main

    # myMath = Math.Math()
    myMath = Math()
    print(myMath.solv(10))