person = {'name': 'zhangsan', 'age': 18, 'age': 22}

# 查找数据（字典的数据在保存时，是无序的） 不能通过下标来获取
print(person['name'])  # zhangsan 使用key获取到对应的value
print(person['age'])  # 22 重复key后面的会覆盖前面的
# print(person['height']) # 如果要查找的key不存在，会直接报错

# 需求:获取一个不存在的key时，不报错，返回默认值
# 使用字典的get方法，如果key不存在，会默认返回None，而不报错
print(person.get('height'))  # None
# 如果根据key获取不到value，使用给定的默认值
print(person.get('gander', 'man'))  # man 找不到返回给定默认值
print(person.get('name', 'lisi'))  # zhangsan

print(person)
