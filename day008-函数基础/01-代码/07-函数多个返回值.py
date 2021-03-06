def test(a,b):
    x = a // b
    y = a % b

    # return语句表示一个函数的结束
    # 一般情况下，一个函数最多只会执行一个return语句
    # 特殊情况（finally语句），一个函数可能会执行多个return语句
    # return [x, y]
    # return {'x':x, 'y':y}
    # return (x, y)
    return x, y  # 返回的数据本质上是元组

result = test(13,5)
print(result)  # (2, 3)

shang, yushu = test(16, 5)
print('商是{}，余数是{}'.format(shang,yushu))  # 商是3，余数是1