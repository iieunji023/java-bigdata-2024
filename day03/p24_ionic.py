# file: p24_ionic.py
# desc: 클래스 상속
from p22_carClass import Car

class Ionic(Car):       # 상속. Car클래스를 상속받아서 ionic
    __fuelRate = 0.0    # 연비

    def setFuelRate(self, rate):
        self.__fuelRate = rate

    def getFuelRate(self) -> float:
        return self.__fuelRate
    
    def getCarNum(self) -> str:     # 함수 오버라이딩
        return f'소중한 제 차는 {super().getCarNum()} 입니다'

myCar = Ionic('54라 9337')
myCar.company = '기아자동차'
myCar.setFuelRate(23.5)
print(myCar)
print(f'내 차의 연비는 {myCar.getFuelRate()} km/1 입니다.')