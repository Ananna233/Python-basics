# +：可以用来拼接，用于字符串、元组、列表
print('hello' + 'world')  # helloworld
print(('good', 5) + ('hi', True))  # ('good', 5, 'hi', True)
print([1, 2, 3] + [4, 5, 6])  # [1, 2, 3, 4, 5, 6]

# - :只能用于集合，求差集
print({1, 2, 3} - {3})  # {1, 2}

# * :可以用于字符串、元组、列表，表示重复多次。不能用于字典和集合(原因是不允许重复)
print('hello' * 3)  # hellohellohello
print([1, 2, 3] * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print((1, 2, 3) * 3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# in :成员运算符
print('a' in 'abc')  # Ture
print(1 in [1, 2, 3])  # Ture
print(4 in (6, 4, 5))  # Ture
print(5 in {3, 4, 5})  # Ture
# in 用于字典是用来判断key是否存在
print('zhangsan' in {'name': 'zhangsan', 'age': 18, 'score': 98, 'tel': '13812342679', 'gender': 'female'})  # False
print('name' in {'name': 'zhangsan', 'age': 18, 'score': 98, 'tel': '13812342679', 'gender': 'female'})  # True

# 带下标的遍历 enumerate 类的使用，一般用于列表和元组等有序的数据
nums = [65, 89, 12, 37, 68, 15, 78]
# nums = (65, 89, 12, 37, 68, 15, 78)
en = enumerate(nums)
for i, e in en:
    print('%d个数据是%d' % (i, e))

# 字典也可以
person = {'name': 'zhangsan', 'age': 18, 'score': 98, 'tel': '13812342679', 'gender': 'female'}  # False

for i, e in enumerate(person):
    print(i, e)  # 下标和key  0 name....
