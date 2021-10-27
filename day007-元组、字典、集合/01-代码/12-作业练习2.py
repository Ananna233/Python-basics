# 　用三个元组表示三门学科的选课学生名字（一个学生可以选多门课）
# （1）求选课 学生总共有多少人
# （2）求值选了第一个学科的人的数量和对应的名字
# （3）求只选一门学科的学生的数量和对应的名字
# （4）求只选两门学科的学生的数量和对应的名字
# （5）求选了三门学科的学生的数量和对应的名字
sing = ('李白', '白居易', '李清照', '杜甫', '王昌龄', '王维', '孟浩然', '王安石')
dance = ('李白', '李商隐', '杜甫', '白居易', '岑参', '王昌龄')
rap = ('李清照', '刘禹锡', '岑参', '王昌龄', '苏轼', '王维', '李白')

# （1）求选课 学生总共有多少人
# 元组之间支持加法运算
total = sing + dance + rap
print(total)
# 使用集合set可以去重
x = set(total)
print(x)
print('学生总数%d人' % len(x))  # 学生总数12人

# （2）求值选了第一个学科的人的数量和对应的名字
only_sing = []
for i in sing:
    if i not in dance and i not in rap:
        only_sing.append(i)
print('只选第一个学科的有{}人，是{}'.format(len(only_sing), only_sing))  # 只选第一个学科的有2人，是['孟浩然', '王安石']

# （3）求只选一门学科的学生的数量和对应的名字
# （4）求只选两门学科的学生的数量和对应的名字
# （5）求选了三门学科的学生的数量和对应的名字
total = sing + dance + rap
p_dict = {}  # 空字典
for name in total:
    if name not in p_dict:
        p_dict[name] = total.count(name)
print(p_dict)

# 只选一门
# 只选两门
# 只选三门
onlyone = []
onlytwo = []
onlythree = []
for i in p_dict.items():
    if i[1] == 1:
        onlyone.append(i[0])
    elif i[1] == 2:
        onlytwo.append(i[0])
    else:
        onlythree.append(i[0])
print('只报了一门的有{}人，分别是{}'.format(len(onlyone), onlyone))
print('只报了两门的有{}人，分别是{}'.format(len(onlytwo), onlytwo))
print('只报了三门的有{}人，分别是{}'.format(len(onlythree), onlythree))
