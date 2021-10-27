# 1.区间判断
# 在一些语言里，判断区间不能连写，需要逻辑运算符链接  60>=score and score>=0
# python 里可以使用连续的区间判断


# 2.隐式类型转换
if 4: # if 后面需要的是一个bool类型的值，如果不是，会自动转换为布尔类型
    print('hello world')

# 3.三元表达式（对if...else语句的简写）
num1 =int(input('please input num1:'))
num2 =int(input('please input num2:'))
x = num1 if num1 > num2 else num2
print ('output the max num in num1 and num2:',x)