# 返回值就是函数执行的结果，并不是所有的函数都必须要有返回值
def add(a,b):
    c = a + b  # 变量c在外部是不可见的，只能在函数内部使用
    return c  # return表示返回函数执行结果

# 获取到add函数的结果，然后再求4次方
result = add(1,3)
print(result**4)  # 256

# 如果一个函数没有返回值，他的返回值就是None
x = print('hello')
print(x)  # None

age = input('请输入你的年龄：')
print(age)  #