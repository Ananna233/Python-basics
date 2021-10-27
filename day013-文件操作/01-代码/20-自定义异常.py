# p201
# 系统内置异常
# ZeroDivisionError  : 除于0的异常  1/0
# FileNotFoundError  : 文件不存在异常 open('xxx.txt')
# FileExistsError    : 多次创建同名的文件夹 os.mkdir('test')
# ValueError         : int('hello')
# KeyError           : person = {'name'='zhangsan'}  person['age']
# SyntaxError        : 语法错误
# IndexError         : 索引错误

# 要求:让用户输入用户名和密码，如果用户名和密码的长度在6~12位为正确，否则为错误
class LenghtError(Exception):  # 自己定义一个异常
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '长度必须在{}至{}之间'.format(self.x, self.y)


password = input('请输入你的密码:')
n = 6
m = 12
if n <= len(password) <= m:
    print('密码正确')
else:
    # 使用raise关键字可以抛出一个异常
    # raise ValueError('密码错误')
    raise LenghtError(n, m)

# 把密码保存到数据库里
print('将密码保存到数据库中')
