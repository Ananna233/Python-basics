# 建立一个汽车类Auto
# 包括轮胎个数，汽车颜色，车身重量，速度等熟悉，并通过不同的构造方法创建实例
# 至少要求 汽车能够加速 减速 停车，再定义一个小汽车类CarAuto 继承Auto 并添加空调、CD属性
# 并且重新实现方法覆盖加速、减速的方法

class Auto(object):
    def __init__(self, color, weight, speed=0, wheel_count=4):
        self.color = color
        self.weight = weight
        self.speed = speed
        self.wheel_count = wheel_count

    def change_speed(self, x):
        self.speed += x
        if self.speed == 0:
            print('停车')


class CarAuto(Auto):
    def __init__(self, color, weight, ac, cd, speed=0, wheel_count=4):
        super(CarAuto, self).__init__(color, weight, speed, wheel_count)
        self.ac = ac
        self.cd = cd


car = Auto('黑色', 1.6)

car.change_speed(30)
print(car.speed)

car.change_speed(-40)
print(car.speed)

car.change_speed(10)

car2 = CarAuto('白色', 2.0, '美的', 'aaa', 10, 5)
