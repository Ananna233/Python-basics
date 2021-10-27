# 使用内置函数 chr 和 ord 能够查看数字和字符的对应关系
# ord 获取字符对应的编码； chr 根据编码获取对应的字符
print(ord('a'))   # 97
print(chr(65))    # A
print(chr(20320)) # 你

# GBK utf-8 BIG5
# 使用字符串encode 方法，可以将字符串转换成为指定编码集结果
#　如果有一个编码集的结果，想把他转换成为对应的字符，可以使用decode
# GBK编码，一个汉字占两个字节
print('你'.encode('gbk')) # b'\xc4\xe3'        0b11000100 11100011
# utf-8编码，一个汉字占3个字符
print('你'.encode('utf-8')) # b'\xe4\xbd\xa0'  0b11100100 10111101 10100000

x = b'\xe4\xbd\xa0'
print(x.decode('utf8')) # 你