a = 100 # 这是个全局变量，在整个py文件里都可以访问

def test1():
    x = 'hello'  # 函数内部定义的局部变量，智能在函数内部使用
    print('x={}'.format(x))  #  hello
    print('函数内部访问a={}'.format(a))  # 函数内部访问a=100

print('函数外部访问a={}'.format(a))  # 函数外部访问a=100
test1()

print('---------------')
a2 = 100 # 这是个全局变量，在整个py文件里都可以访问
word = 'hello'

def test2():

    # 如果局部变量的名和全局变量同名，会在函数内部又定义一个新的局部变量
    # 而不是修改全局变量
    a2 = 55
    print('函数内部的a2={}'.format(a2))  # 函数内部的a2=55

    # 函数内部如果想要修改全局变量
    # 使用global对变量进行声明，可以通过函数修改全局变量的值
    global word
    word ='ok'

    print('locals = {},globals = {}'.format(locals(),globals()))

test2()
print('函数外部的a2={}'.format(a2))  # 函数外部的a2=100
print('函数外word={}'.format(word))  # 函数外word=ok

# 内置函数  global()可以查看全局变量    locals()可以查看局部变量

# 在Python里，只有函数能够分割作用域