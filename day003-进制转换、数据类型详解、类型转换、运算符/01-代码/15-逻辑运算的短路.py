# 逻辑与运算，只有所有运算数是True，结果才是True
# 只要有一个是False，结果就是False
4 > 3 and print('hello wrold') # hello world
4 < 3 and print('你好世界')
# 逻辑与运算的短路问题，前面错了，后面就不会再执行

# 逻辑或运算，只有所有的运算数是False，结果才是False
# 只要有一个运算数是True，结果就是True
4 > 3 or print('哈哈哈')
4 < 3 or print('嘿嘿嘿') # 嘿嘿嘿
# 对了一个后面就不会再运行

# 逻辑运算的结果，一定是布尔值吗？  不一定
# 逻辑与运算做取值时，取第一个为False的值，如果所有的运算数都是True，取最后一个值
print(3 and 5 and 0 and 'hhh')  # 0
print('hello' and 100 and '你好') # 你好

# 逻辑或运算做取值时，取第一个为True的值；如果所有的运算数都是False，取最后一个值
print(0 or [] or 'hhh' or 6 or 'nnihao') # hhh
print(0 or [] or {} or ())  # ()