 # 有一个列表names,保存了一组姓名names=['zhangsan','lisi','chirs','tony','jack']
# 再让用户输入一个姓名，如果这个姓名在列表里存在，提示用户姓名已存在
# 如果这个姓名不存在，就将这个姓名添加到列表里

names = ['zhangsan', 'lisi', 'chirs', 'tony', 'jack']
username = input('please input a name:')

# if username in names:
#     print('the username have existed in names')
# else:
#     names.append(username)
# print(names)

# 遍历法  for...else 语句
for name in names:
    if username == name:
        print('The username have existed in names')
        break
else:
    names.append(username)
print(names)

# 统计列表里出现次数最多的元素
# 求列表里最大数
# 删除列表里空字符串
# 冒泡优化