# 缺省参数要放在后面
def say_hello(name,age,city='广州'):  # 形参city设置了默认值
    print('大家好，我是{}，今年{}，我来自{}'.format(name,age,city))


say_hello('tony',20)  # 大家好，我是tony，今年20，我来自广州
say_hello('anan',18,'北京')  # 大家好，我是anan，今年18，我来自北京

# 如果有位置参数【如下面的'Jake'，一一对应】和关键字参数【如下age=21】，关键字参数一定要放在位置参数的后面
say_hello('Jake',age=21,city='浙江')  # 可以直接传递单个参数，也可以使用变量赋值的形式传参

# 缺省参数：
# 有些函数的参数是，如果你传递了参数，就是用传递的参数
# 如果没有传递参数，就使用默认的值

# print函数里的end 就是缺省参数