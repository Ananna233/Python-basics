# Python里使用print内置函数输出内容

# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# sep 参数用来表示输出时，每个值之间使用何种字符作为分隔，默认使用空格作为分隔符
# end 当执行完一个print语句后，接下来要输出的字符，默认\n表示换行
# file 输出位置
print('hello','hi','good')
print('hello','hi','good',sep='+',end='<<<<<<<<<<')  # hello+hi+good<<<<<<<<<<hi,你好呀
print('hi,你好呀')