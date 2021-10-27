# 没有设置了__all__ 使用 from <module_name> import *
# 会导入除了以_开始的所以变量和函数

x = 'hello'
y = 1000

# 以一个下划线开始的变量，建议只在本模块使用，别的模块不要使用

_age = 19  #  from <module_name> import *这种方法无法导入

# import hello  方法也是可以调用的