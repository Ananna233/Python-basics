person = {'name': 'zhangsan',
          'age': 18,
          'height': 180,
          'age': 20,  # 会替换上一个age
          'ispass': True,  # 可以是布尔值
          'hobbies': ['唱', '跳', 'rap', '篮球'],  # 也可以是列表
          1: 'good',  # key是不可变类型
          ('hello', 'world'): 100
          }

# 1、字典里的key不允许重复，如果key重复了，后一个key对应的值会覆盖前一个
# 2、字典里的value可以是任意数据类型，但key只能使用不可变数据类型，一般使用字符串
print(person)  # {'name': 'zhangsan', 'age': 20, 'height': 180, 'ispass': True, 'hobbies': ['唱', '跳', 'rap', '篮球'], 1: 'good', ('hello', 'world'): 100}
