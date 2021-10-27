nums = [1,2,[100,200,600],5,7,8] # 列表的嵌套

import random

# 一个学校，有3个办公室，现在有10个老师，完成随机分配
teachers = ['A','B','C','D','E','F','G','H','I','J']
rooms = [[],[],[]]

for teacher in teachers:
    room = random.choice(rooms) # choice 从列表里随机选择一个数据
    room.append(teacher)

print(rooms)

# 带下标我们一般使用while
# for循环也可以带下标
for i,room in enumerate(rooms):
    print('房间%d里一共有%d个老师,分别是:' %(i,len(room)),end='')
    for teacher in room:
        print(teacher,end=' ')
    print()