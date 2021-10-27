# 写出判断一个数能否同时被3和7整除的条件语句，并且打印对应的结果
num = int(input('请输入一个数字：'))

if num % 3 ==0 and num % 7 ==0:
    print(num,'能够被3和7整除')

# 写出判断一个数能被3或7整除，但不能同时被3和7整除的条件语句，并且打印对应的结果
num2 = int(input('请输入一个数字：'))

if (num2 % 3 ==0 or num2 % 7 ==0) and (num2 % 21 != 0):
    print(num2,'能够被3或7整除，但不能同时被3和7整除')

# 假设今天的上课时间是15678秒，编程计算今天的上课时间是多少小时，多少分钟，多少秒；以xx时xx分xx秒的方式表示
x = 15678
hour = x // 3600
min = x % 3600 // 60
second = x % 60
print(hour,'hour',min,'min',second,'second')  # 4 hour 21 min 18 second