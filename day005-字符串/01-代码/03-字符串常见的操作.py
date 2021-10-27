x = 'abcdefghijklmnjj'

# 使用内置函数 len 获取字符串长度
print(len(x)) # 14

# 查找内容相关的方法 find/index/rfind/rindex 可以获得指定字符的下标
print(x.find('j'))  # 9  返回找到的最小的下标
print(x.index('j')) # 9  返回找到的最小的下标

print(x.find('z'))    # -1 如果字符串不存在，返回结果是-1
# print(x.index('z')) # substring not found 字符不存在会报错

print(x.rfind('j'))  # 15  返回找到的最大的下标
print(x.rindex('j')) # 15  返回找到的最大的下标

# startswith,endswith,isalpha,isdigit,isalnum,isspace
# is开头的是判断，结果是一个布尔类型
print('hello'.startswith('h'))  # True
print('hello'.startswith('he')) # True 'hello'是以'he'开头的
print('hello'.endswith('o'))    # True
# isalpha 是否由字母组成
print('hello'.isalpha())    # True alpha 表示字母
print('hello233'.isalpha()) #　False
# isdigit 是否由数字组成
print('123'.isdigit())      # True digit 表示数字
print('good123'.isdigit())  # False
print('3.14'.isdigit())     # False
# isalnum 是否由数字字母组成
print('123hello'.isalnum()) # True isalnum
print('hello'.isalnum())    # True
print('123'.isalnum())      # True
print('3.14'.isalnum())     # False
# isspace 是否全是由空格组成
print('      '.isspace())   # True
print('  haha '.isspace())  # False
# 计数
# count 返回str在start和end之间在字符串里面出现的次数
# 语法结构 S.count(sub[,start[,end]])  ->int
mystr = '你好呀你你哈哈哈好你'
print(mystr.count('你'))  # 4
# 替换
# replace 方法 ：用来替换字符串
wold ='hello'
wold.replace('l','x') # repalce 将字符串里的l 替换成x
print(wold) # hello  字符串是不可变数据类型！
newwold = wold.replace('l','x') #
print(newwold) # hexxo 原来的字符串不会改变，而是生成一个新的字符串来保存替换后的结果
m = 'ananna'
newm = m.replace('a','b',2) # 指定替换次数，，，不超过count次
print(newm) #　bnbnna
