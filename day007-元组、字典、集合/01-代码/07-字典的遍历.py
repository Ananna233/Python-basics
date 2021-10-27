person = {'name': 'zhangsan', 'age': 19, 'height': 181, 'addr': 'shanghai'}
# 列表和元组是单一的数据，但是字典是键值对的形式

# 第一种遍历方式
# for...in...循环获取的是key
# for i in person:
#     print(i,end=' ') # name age height addr
for i in person:
    print(i, '=', person[i])

# 第二种方式：获取所有的key，然后再遍历key，根据key获取value
print(person.keys())  # dict_keys(['name', 'age', 'height', 'addr'])
for i in person.keys():
    print(i, '=', person[i])

# 第三种方式：获取所有的value
# 只能拿到值，不能拿到key
for i in person.values():
    print(i)

# 第四种方式：
# print(person.items()) # dict_items([('name', 'zhangsan'), ('age', 19), ('height', 181), ('addr', 'shanghai')])
# for item in person.items():
#     # 列表里面的元素是元组，把元组当做整体进行遍历
#     print(item[0],'=',item[1])
for k, v in person.items():
    print(k, '=', v)
