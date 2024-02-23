# file: p23_carSample.py
# desc: Car클래스 사용해보기

from p22_carClass import Car

myCar = Car('54라 9538')   # 클래스를 사용, 객체를 하나 생성(instance)
yourCar = Car('98호 8733')


# myCar.__carNum = '54라 9538' -> __carNum으로 private 접근 제한되었으므로 더이상 사용불가
myCar.company = '현대자동차'
myCar.fuelType = '가솔린'
myCar.carType = '하이브리드'
myCar.color = '흰색'
myCar.releaseYear = 2018
yourCar.__carNum = '87호 8733'

print(myCar)
print(yourCar)

myCar.getCarColor()
myCar.start()
myCar.accel()
yourCar.start()
myCar.turnLeft()
myCar.turnRight()
myCar.brake()