#
import random # 导入模块
player = int(input('请输入 (0)剪刀  （1）石头  （2）布'))

# input 是用来接受用户输入的数据
# 电脑随机产生一个数据
# 使用随机数模块 random
# random.randint(a,b)==>能够产生[a,b]的整数
computer = random.randint(0,2)
print('compute 出的是',computer)

if (player == 0 and computer == 2) or (player ==1 and computer == 0) or (player == 2 and computer ==1):
    print('你赢了')
elif player == computer:
    print ('平局')
else:
    print('你输了')