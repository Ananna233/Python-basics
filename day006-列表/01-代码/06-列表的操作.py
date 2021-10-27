# 列表是用来保存多个数据的，是有序可变的
# 操作列表，一般包含增加数据、删除数据、查询数据以及修改数据
# 增删查改

heros = ['小乔','嬴政','韩信','露娜','后羿','亚瑟','李元芳']

# 添加元素的方法 append insert extend
# append 在列表的最后追加一个数据
heros.append('黄忠')
print(heros) # ['小乔', '嬴政', '韩信', '露娜', '后羿', '亚瑟', '李元芳', '黄忠']

# insert（index,object） 需要两个参数
# index 表示下标，在哪个位置前插入数据
# object 表示对象，具体插入哪个数据
heros.insert(3,'李白')
print(heros) # ['小乔', '嬴政', '韩信', '李白', '露娜', '后羿', '亚瑟', '李元芳', '黄忠']

x = ['狄仁杰','钟馗','武则天']
# extend(iterable) 需要一个可迭代对象
# A.extend(B)  ==>  将可迭代对象B添加到A里
heros.extend(x)
print(heros) # ['小乔', '嬴政', '韩信', '李白', '露娜', '后羿', '亚瑟', '李元芳', '黄忠', '狄仁杰', '钟馗', '武则天']
print(x)     # ['狄仁杰', '钟馗', '武则天']  x 是不会被改变的

# ?
heros.insert(3,x)
print(heros)