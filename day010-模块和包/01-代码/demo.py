__all__ = ['m', 'test']
# 设置了__all__ 使用 from <module_name> import * 只会导入__all__ 里面的变量和函数
m = 'yes'
n = 100


def test():
    print('我是demo里的test函数')


def foo():
    print('我是demo里的foo函数')


def division(a, b):
    return a / b

# __name__:当直接运行这个py文件的时候，值是__main__
# 如果这个py文件作为一个模块导入的时候，值是文件名
# 要想测试代码只在运行这个py文件时才起作用
if __name__ == '__main__':
    print('demo里的name是:',__name__)
    print('测试一下division函数，结果是：', division(4, 2))
