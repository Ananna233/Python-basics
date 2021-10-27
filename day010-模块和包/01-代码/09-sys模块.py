# sys 系统相关的功能
import sys

print('hello world!')
# sys.exit(100)  # 退出程序，和内置函数exit功能一致
print('你好呀')

print(sys.path)  # 结果是一个列表，表示查找模块的路径
#['D:\\Python基础学习\\day010-模块和包\\01-代码',
# 'D:\\Python基础学习\\day010-模块和包\\01-代码',
# 'D:\\Python\\python38.zip',
# 'D:\\Python\\DLLs',
# 'D:\\Python\\lib',
# 'D:\\Python',
# 'D:\\Python\\lib\\site-packages']

# sys.stdin  # 可以像input一样，接收用户的输入  接收用户的输入，和input相关

# sys.stdout 和 sys.stderr 默认都是在控制台
# sys.stdout  # 修改sys.stdout 可以改变默认输出位置
# sys.stderr  # 修改sys.stderr 可以改变错误输出的默认位置