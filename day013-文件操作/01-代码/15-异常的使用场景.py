age = input('请输入你的年龄：')  # input 接受的的用户输入是一个字符串

# if age.isdigit():  只能判断是int
try:
    age = float(age)
except ValueError as e:
    print('输入的不是数字')
else:
    if age > 18:
        print('欢迎来到我的网站')
    else:
        print('未满十八岁')
