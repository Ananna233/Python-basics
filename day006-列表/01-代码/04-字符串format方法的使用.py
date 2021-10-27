# {} 也可以占位

# {} 里面什么都不写，会读取后面的内容，一一对应填充
x = '大家好，我是{}，我今年{}岁了'.format('anan', 18)
print(x)  # 大家好，我是anan，我今年18岁了

# {数字}根据数据的顺序填入，数字从0开始
y = '大家好，我是{1}，今天{0}岁了'.format(18, 'banana')
print(y)  # 大家好，我是banana，今天18岁了

# {变量名}
z = '大家好，我是{name}，我今年{age}岁了，我住在{addr}'.format(age=18,addr='广州',name='anan')
print(z) # 大家好，我是anan，我今年18岁了，我住在广州

# 混合使用{数字} {变量} 变量名name必须放最后
a = 'hello，我是{name},我今年{1}岁了，我来自{0}'.format('泰国',20,name='tony')
print(a) # hello，我是tony,我今年20岁了，我来自泰国

B = ['zhangsan',18,'上海',180]
# b = "hello,我是{},今年 {}岁了,来自{}，身高{}".format(B[0],B[1],B[2],B[3])
b = "hello,我是{},今年 {}岁了,来自{}，身高{}".format(*B)
print(b) # hello,我是zhangsan,今年 18岁了,来自上海，身高180

info = {'name':'anan','age':20,'addr':'北京','height':180}
c = 'hello ,我是{name}，我来自{addr}，今年{age}碎了，身高{height}cm'.format(**info)
print(c) # hello ,我是anan，我来自北京，今年20碎了，身高180cm