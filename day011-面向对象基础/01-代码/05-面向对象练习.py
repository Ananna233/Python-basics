# 房子（House）有 户型、总面积、剩余面积(总面积60%)和家具名称列表属性
# 新房子没有任何的家具
# 将家具的名称追加到家具名称列表中
# 判断家具的面积 是否超过剩余面积，如果超过，提示不能添加这件家具

class House(object):
    def __init__(self, house_type, total_area, fru_list=None):
        if fru_list is None:  # 如果这个值是None
            fru_list = []  # 将fru_list设置为空列表
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.6
        self.fru_list = fru_list

    def add_fru(self, x):
        if self.free_area < x.area:
            print('剩余面积不足，{}放不进去'.format(x.name))
        else:
            self.fru_list.append(x.name)
            self.free_area -= x.area
    def __str__(self):
        return '户型={}，总面积={}，剩余面积={}，家具列表={}'.format(self.house_type,self.total_area,self.free_area,self.fru_list)
        # 调用返回字符串打印

# 家具（Furniture） 有名字和占地面积属性，其中
# 席梦思（bed） 占地4平米
# 衣柜（chest）占地 2平米
# 餐桌（table） 占地1.5平米
# 将以上三件家具添到房子中
# 打印房子 时，要求输出户型，总面积，剩余面积，家具名称列表
class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


# 创建房间对象的时候，传入户型和总面积
house1 = House('两室一厅', 56)
# 把家具添加到房间里（面向对象关注点:让谁做）

bed = Furniture('席梦思', 4)
chest = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)

house1.add_fru(bed)
house1.add_fru(chest)
house1.add_fru(table)

print(house1)  # print 打印一个对象的时候，会调用这个对象的__repr__或者__str__方法，获取它们的返回值
# 实际上就是print(house.__str__)


house2 = House('一室一厅', 20)
# 把家具添加到房间里（面向对象关注点:让谁做）

bed = Furniture('席梦思', 4)
chest = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)
sofa = Furniture('沙发',10)

house2.add_fru(sofa)
house2.add_fru(bed)
house2.add_fru(chest)
house2.add_fru(table)

print(house2)  # print 打印一个对象的时候，会调用这个对象的__repr__或者__str__方法，获取它们的返回值
# 实际上就是print(house.__str__)