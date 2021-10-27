class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        print('__eq__方法被调用了，other=', other)
        if self.name == other.name and self.age == self.age:
            return True
        return False


# 1. 调用__new__方法申请内存空间
p1 = Person('zhangsan', 18)
p2 = Person('zhangsan', 18)

# p1 p2 不是同一个对象
# 怎样比较两个对象是否是同一个对象？比较的是内存地址
print('p1地址:0x%X' % id(p1))  # p1地址:0x22070545520
print('p2地址:0x%X' % id(p2))  # p2地址:0x22070526730

# is 身份运算符 可以用来判断两个对象是否是同一个对象
print('p1 is p2', p1 is p2)  # p1 is p2 False
print('p1 == p2', p1 == p2)  # p1 == p2 False
# p1 == p2 本质是调用p1.__eq__(p2) 返回return结果 如果不重写，默认比较依然是内存地址

# is 比较两个对象的内存地址
# == 会调用__eq__方法，获取这个方法的比较结果
# nums1 = [1, 2, 3]
# nums2 = [1, 2, 3]
# print(nums1 is nums2)  # False
# print(nums1 == nums2)  # True
