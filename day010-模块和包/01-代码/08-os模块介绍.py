# os全称 OperationSystem操作系统
# os 模块里提供的方法就是用来调用操作系统里的方法
import os

# os.name  ==> 获取操作系统的名字  Windows系列==>nt  /非Windows ==>posix
print(os.name)  # nt
print(os.sep)  # \ 路径的分割符 Windows \  非Windows /

# os模块里的 path 是经常使用的
# abspath ==>获取文件的绝对路径
print(os.path.abspath('01-闭包的概念.py'))  # D:\Python基础学习\day010-模块和包\01-代码\01-闭包的概念.py

# isdir 判断是否是文件夹
print(os.path.isdir('02-计算一段代码的执行时间.py'))  # False
print(os.path.isdir('anan'))  # True

# isfile 判断是否是文件
print(os.path.isfile('03-优化计算时间的代码.py'))  # True
print(os.path.isfile('anan'))  # False

# exists 判断是否存在
print(os.path.exists('05-装饰器的详解.py'))  # True
print(os.path.exists('mmm.py'))  # False

# 获取文件名和后缀名
file_name = '2020.9.24.demo.py'
# print(file_name.rpartition('.'))  # ('2020.9.24.demo', '.', 'py')
print(os.path.splitext(file_name))  # ('2020.9.24.demo', '.py')

# os 里其他方法的介绍
# os.getcwd()  # 获取当前的工作目录，既当前Python脚本工作的目录
# os.chdir('test')  # 改变当前脚本工作目录，相当于shell下的长度、命令
# os.rename('毕业论文.txt','毕业论文-最终版.txt')  # 文件重命名
# os.remove('毕业论文.txt')  # 删除文件
# os.rmdir('demo')  # 删除空文件夹
# os.removedirs('demo')  # 删除空文件夹
# os.mkdir('demo')  # 创建一个文件夹
# os.chdir('C:\\')  # 切换工作目录
# os.listdir('C:\\')  # 列出指定目录里的所有文件和文件夹
# os.name  # nt==>windows  posix ==>linux/Unix 或者MacOS
# os.environ  # 获取到环境配置
# os.environ.get('PATH')  # 获取指定的环境配置

# 交互式运行
# Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
# import os
# os.getcwd()
# 'D:\\Python基础学习\\day010-模块和包\\01-代码'
# os.chdir('../')
# os.getcwd()
# 'D:\\Python基础学习\\day010-模块和包'
# os.listdir()
# ['01-代码']
