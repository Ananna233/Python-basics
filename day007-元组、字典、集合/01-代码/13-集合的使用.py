# 集合是一个不重复的无序的，可以使用{}或者set表示
# {}有两种意思：字典、集合
# {}里面放的是键值对，他就是一个字典；如果{}放的是单个的值，就是一个集合
person = {'name': 'zhangsan', 'age': 18}  # 字典
x = {'hello', 'world', 18}  # 集合

# 如果有重复的数据，会自动去除   且无序
names = {'zhangsan', 'lisi', 'tony', 'make', 'tony'}
print(names)  # {'lisi', 'zhangsan', 'make', 'tony'}

# 增加一个元素
# add()
names.add('anan')
print(names)  # {'zhangsan', 'tony', 'make', 'anan', 'lisi'}

# 随机删除一个
# .pop()
names.pop()
print(names)  # {'make', 'tony', 'zhangsan', 'lisi'}

# 删除一个指定的元素,,如果没有回报错
# remove()
names.remove('tony')
print(names)  # {'make', 'lisi', 'anan'}

# union  将多个集合合并生成一个新的集合
# 原集合不会变化
a = names.union({'花花', '小爱'})
print(a)  # {'zhangsan', '花花', 'anan', '小爱', 'lisi'}

# A.update(B) 将B拼接到A里
names.update({'青青', '小白'})
print(names)  # {'make', '小白', 'lisi', 'anan', '青青'}

# 没有查询方法

# 清空一个集合
names.clear()
# 空集合的表示方式不是{}，{}表示的是空字典
# 空集合 set()
print(names)  # set()
