# 编写一个函数，求多个数中的最大值
def get_max(*args):
    x = args[0]
    for i in args:
        if i > x:
            x = i
    return x


print('max=', get_max(1, 5, 9, 6, 3, 4, 96, 311))  # max= 311
print('-------------------------')

# 编写一个函数，实现摇色子的功能，打印N个色子的点数和
import random


def get_sum(n):
    m = 0
    for i in range(n):
        m = m + random.randint(1, 6)
    return m


# n = int(input('摇色子个数是n='))
# print('{}个色子和是{}'.format(n, get_sum(n)))
print('-----------------------')


# 编写一个函数，提取指定字符串中所有的字母，然后拼接在一起产生一个新的字符串
def get_alphas(word):
    new_str = ''
    for i in word:
        if i.isalpha():
            new_str += i
    return new_str


word = '123hello665.;world'
print(word, '字符串里的字母是', get_alphas(word))  # 123hello665.;world 字符串里的字母是 helloworld
print('----------------------')


# 写一个函数，默认求10的阶乘，也可以求其他数字的阶乘
def get_factorial(n=10):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


n = 11
print(n, '的阶乘=', get_factorial(n))  # 123hello665.;world 字符串里的字母是 helloworld
print('------------------')


# 写一个函数，求多个 数的平均值
def get_average(*args):
    x = 0
    for i in args:
        x += i
    return x / len(args)


print('1, 2, 3, 4, 5, 6, 7, 8,9的平均值=', get_average(1, 2, 3, 4, 5, 6, 7, 8, 9))  # 1, 2, 3, 4, 5, 6, 7, 8,9的平均值= 5.0
print('--------------------*')


# 写一个自己的capitalize函数，能够将指定字符串的首字母变成大写字母
def my_capitalize(word):
    c = word[0]
    if 'a' <= c <= 'z':
        new_str = word[1:]
        return c.upper() + new_str  # 实际上c是不变的，需要用一个东西接住变大写的c.upper()
    return word


word3 = 'hello'
print('word3={},转变后={}'.format(word3, my_capitalize(word3)))  # word3=hello,转变后=Hello
print('-------------------')


# 写一个自己的endswith函数，判断一个字符串是否以指定的字符串结尾
def my_endswith(ord_str, str1):
    return ord_str[-len(str1):] == str1


print('hello he llo==>', my_endswith('hello', 'llo'))  # hello he llo==> True
print('*******************************')


# 写一个自己的isdigit函数，判断一个字符串是否是纯数字字符串
def my_isdigit(str):
    for m in str:
        if not '0' <= m <= '9':
            return False
    return True


print('6466a68是纯数字字符串吗', my_isdigit('6466a68'))  # 6466a68是纯数字字符串吗 False
print('-------------')


# 写一个自己的upper函数，将一个字符串中所有的小写字母变成大写字母
# 'a' ==>97  'A' ==> 65
# ord()  将字符转为ascII码   chr()将ASCII码转为字符
def my_upper(str):
    new_str = ''
    for i in str:
        if 'a' <= i <= 'z':
            i = chr(ord(i) - (ord('a') - ord('A')))
        new_str += i
    return new_str


print(my_upper('hellO233Ahh'))  # HELLO233AHH
print(chr(66))
print('***************************')


# 写一个函数实现自己in操作，判断指定序列中，指定元素是否存在
def my_in(it, ele):
    for i in it:
        if i == ele:
            return True
    return False


print(my_in(['zhangsan', 'lisi', 'tony'], 'lisi'))  # True
