# 一个模块本质上就是一个py文件
# 自己定义一个模块，其实就是自己写的一个py文件
# 如果一个py文件想要当做一个模块被导入，文件名一定要遵守命名规范
# 由数字、字母、下划线组成，不能以数字开头

# 分屏：右击名字 选择Split Vertically

# 导入了一个模块，就能使用模块里的变量和函数
import my_module

# 使用from <module_name> import * 导入这个模块里“所有”的变量和函数
# 本质是读取模块里的__all__属性，看这个属性里定义了哪些变量和函数
# 如果模块里没有定义__all__才会导入所有不以_开头的变量和函数
# 使用这个语法，这样的话，函数里面有__all__,__all__   all里面有的才能用
# 把模块导入（import） ,,就一样可以用了  语法是<module.name>.XXX
# 使用from <module_name> import *是直接  XXX
from demo import *  # 使用这两种导入模块都会执行一遍模块代码


print(my_module.a)  # hello
my_module.test()  # 我是my_module模块里的test函数

# 使用from demo import * 写法，不再需要写模块名
# print(n)  # __all__ 里面没有  会出错
print(m)  # yes



# 不建议调用以一个下划线_开始的变量，函数
import hello

print(hello._age)  # 19