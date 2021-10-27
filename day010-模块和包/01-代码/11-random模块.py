# random 模块用来生成一个随机数
import random

# randint(a,b) 用来生成[a,b]的随机整数  等价于randrange(a,b+1)
print(random.randint(2, 9))

# random() 用来生成[0,1)的随机浮点数
print(random.random())

# randrange(a,b) 用来生成[a,b)的随机整数
random.randrange(2, 9)

# choice 用来在可迭代对象里随机抽取一个数据
print(random.choice(['zhangsan','lisi','jack','wangwu','tony','anan']))

# sample 用来在可迭代对象里随机抽取n个数据
print(random.sample(['zhangsan', 'lisi', 'jack', 'wangwu', 'tony', 'anan'], 3))

