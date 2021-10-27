person = {'name': 'zhangsan', 'age': 20, 'addr': 'shanghai'}
print(person['name'])  # zhangsan

# 直接使用key可以修改对应的value
person['name'] = 'lisi'
print(person['name'])  # lisi

# 如果key存在，是修改key对应的value
# 如果key在字典里不存在，会往字典里添加一个新的key-value
person['gender'] = 'female'
print(person)  # {'name': 'lisi', 'age': 20, 'addr': 'shanghai', 'gender': 'female'}

print(type(person))

# 把name对应的键值对删除
a = person.pop('name')
print(person)  # {'age': 20, 'addr': 'shanghai', 'gender': 'female'}
print(a)  # lisi 返回删除的value

# popitem 删除一个元素，结果是被删除的这个元素组成的键值对
b = person.popitem()
print(b)  # ('gender', 'female')
print(person)  # {'age': 20, 'addr': 'shanghai'}

#
del person['addr']
print(person)  # {'age': 20}

# clear 用来清空一个字典
person.clear()
print(person)  # {}
