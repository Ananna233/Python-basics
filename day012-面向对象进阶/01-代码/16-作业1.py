# 设计两个类：
# - 一个点类，属性包括x , y坐标
# - 一个Rectang类（矩形），属性有左上角和右下角坐标
# 方法：1.计算矩形的面积； 2.判断点是否在矩形内
# 实例化一个点对象，一个正方形对象，输出矩形的面积。输出点是否在矩形 内

class Point(object):
    # point 方法在创建时，需要两个int类型的参数，用来表示x ，y坐标
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectang(object):  # 只要在一条对角线上的两角就行
    def __init__(self, top_left: Point, bottom_right: Point):
        if top_left.x != bottom_right.x and top_left.y != bottom_right.y:
            self.top_left = top_left
            self.bottom_right = bottom_right
        else:
            print('输入左上右下角数据不是矩形')

    def get_area(self):
        return abs((self.top_left.x - self.bottom_right.x) * (self.top_left.y - self.bottom_right.y))

    def is_inside(self, point):
        if (point.x - self.top_left.x) * (point.x - self.bottom_right.x) <= 0 and (point.y - self.top_left.y) * (
                point.y - self.bottom_right.y) <= 0:
            print('({},{})在矩形内'.format(point.x, point.y))
        else:
            print('不在矩形内')


p1 = Point(2, 20)
p2 = Point(4, 10)
rec = Rectang(p1, p2)
print(rec.get_area())

p = Point(3, 13)
rec.is_inside(p)


# 计算器
class Calculator(object):
    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(4, 5))
