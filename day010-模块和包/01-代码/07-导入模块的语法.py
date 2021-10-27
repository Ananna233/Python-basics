# 模块：在Python里一个py文件，就可以理解为模块
# 不是所有的py文件都能作为一个模块导入
# 如果想要让一个py文件能够被导入，模块的名字必须遵守命名规则
# Python为了方便我们开发，提供了很多内置模块


import time  # 1、使用import模块直接导入一个模块

from random import randint  # 2、from模块名import函数名，导入一个模块里的方法或变量
randint(0,2)  # 生产【0,2】的随机整数

from math import *  # 3、from 模块名 import *导入这个模块里的“所有”方法和变量
print(pi)

import datetime as dt  # 4、导入一个模块并给这个模块起一个别名
print(dt.MAXYEAR)  # 9999

from copy import deepcopy as dp  # 5、from 模块名 import 函数名 as 别名
c = dp(['hello',[1,2,3],'world',3])  # 深复制
print(c)

# 1,4是导入模块  2，3，5是导入模块里的内容