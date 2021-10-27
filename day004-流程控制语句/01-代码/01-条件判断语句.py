# Python里的条件判断语句 if / if...else / if...elif...elif...else

# if 条件判断:
#   条件成立，执行的代码   一个tab缩进
age = int(input('请输入年龄：'))
if age < 18: # 字符串和数字做比较运算规则：==结果是False，！=是True   其他报错
    print('未满十八，禁止入内')

# if...else语句
# if 判断条件:
#   条件成立时执行的代码
# else :
#   条件不成立时执行的代码
age = int(input('请输入年龄：'))
if age < 18:
    print('未满十八，禁止入内')
else:
    # if的条件不满足是执行的代码
    print('可以上网冲浪')
