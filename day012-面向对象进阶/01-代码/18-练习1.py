# 定义一个点类Pointer
# 属性是横坐标 x 与纵坐标 y

# 定义一个圆类 Circle
# 属性有圆心点cp 与半径 radius
# 方法有：
# 1.求圆的面积
# 2.求圆的周长
# 3.求指定点与圆的关系【圆内、圆外、圆上】

import math


class Pointer(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(object):
    def __init__(self, cp: Pointer, radius):
        self.cp = cp
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_length(self):
        return math.pi * self.radius * 2

    def relationship(self, point: Pointer):
        '''
        distance = (x-x0)**2 + (y-y0)**2 - radius**2
        distance > 0 在圆外  distance == 0 在圆上  distance < 0 在圆内
        :param point: 需要判断的点
        :return:
        '''
        distance = (point.x - self.cp.x) ** 2 + (point.y - self.cp.y) ** 2 - self.radius ** 2
        print('({}, {})'.format(point.x, point.y), end='')
        if distance > 0:
            print('在圆外')
        elif distance == 0:
            print('在圆上')
        else:
            print('在圆内')


p = Pointer(0, 0)  # 创建了一个Pointer对象
p2 = Pointer(3, 4)

c = Circle(p, 5)  # 创建好的Pointer对象传递给了Circle对象c

print(c.get_area())  # 78.53981633974483
print(c.get_length())  # 31.41592653589793
c.relationship(p2)
