persons = [
    {'name': 'zhangsan', 'age': 18},
    {'name': 'lisi', 'age': 20},
    {'name': 'wangwu', 'age': 21},
    {'name': 'tony', 'age': 17}
]

# 让用户输入姓名，如果姓名已经存在，提示用户；如果姓名不存在，继续输入年龄，并存入列表里
yourname = input('please input your name:')

for person in persons:
    # if name in person: # in 运算符，如果直接用在字典上，是用来判断key是否存在，而不是value
    if person['name'] == yourname:
        print('你输入的名字存在')
        break
else:
    print('你输入的名字不存在')
    # 创建一个新的字典 new_person
    new_person = {'name': yourname}

    yourage = int(input('请输入你的年龄：'))
    new_person['age'] = yourage

    # 把这个新的数据存储到person列表里
    persons.append(new_person)
    print('用户添加成功')
print(persons)
