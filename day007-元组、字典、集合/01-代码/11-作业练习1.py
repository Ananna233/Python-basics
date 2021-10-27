#  声明一个列表，在列表中保存6个学生的信息
students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'tel': '13812342679', 'gender': 'female'},
    {'name': 'lisi', 'age': 15, 'score': 89, 'tel': '13825674893', 'gender': 'male'},
    {'name': 'wangwu', 'age': 21, 'score': 98, 'tel': '13825679348', 'gender': 'unknow'},
    {'name': 'chirs', 'age': 21, 'score': 76, 'tel': '13825674587', 'gender': 'male'},
    {'name': 'jack', 'age': 17, 'score': 52, 'tel': '13825674964', 'gender': 'female'},
    {'name': 'tony', 'age': 23, 'score': 91, 'tel': '13825674324', 'gender': 'unknow'},
]

# （1）统计不及格学生的个数
# （2）打印不及格学生的名字和对应的成绩
# （3）统计未成年学生的个数
# （4）打印手机尾号是8的学生的名字
# （5）打印最高分和对应的学生名字
count = 0
teenager_count = 0
max_score = 0
for student in students:
    if student['score'] < 60:
        count += 1
        print('%s不及格，分数是%d' % (student['name'], student['score']))
    if student['age'] < 18:
        teenager_count += 1
    if student['tel'].endswith('8'):
        print('%s的手机号以8结尾' % student['name'])
    if student['score'] > max_score:
        max_score = student['score']

print('不及格的学生有%d' % count)
print('未成年的学生有%d' % teenager_count)

for student in students:
    if student['score'] == max_score:
        print('最高分学生是%s，最高分%d' % (student['name'], student['score']))

# （6）删除性别不明的所有学生（注意有坑）
# 方法一：将不需要删除的数据添加的新的列表
# new_students = [x for x in students if x['gender'] != 'unknow']
# students = new_students
# print(students)

# 方法二：使用for循环倒着删除数据
# i = 0
# for i in range(len(students)-1,-1,-1):
#     if students[i]['gender'] == 'unknow':
#         students.remove(students[i])
# print(students)

# 方法三：使用while循环删除需要删除的数据，补齐因删除数据而导致的列表数据索引变化
# i = 0
# while i <len(students):
#     if students[i]['gender'] == 'unknow':
#         students.remove(students[i])
#         i -= 1
#     i += 1
# print(students)

# 方法四：遍历在新列表操作，删除在原列表操作
# for student in students[:]: # students[:]是student[]的一个切片
#     if student['gender'] == 'unknow':
#         students.remove(student)
# print(students)

# 方法五：使用内建函数filter（）和匿名函数
# new_students = filter(lambda x : x['gender']!='unknow',students)
# print(list(new_students))

# （7） 将列表按学生成绩从大到小排序
for i in range(0, len(students) - 1):
    for j in range(0, len(students) - 1 - i):
        if students[j + 1]['score'] > students[j]['score']:
            students[j + 1], students[j] = students[j], students[j + 1]
print(students)
