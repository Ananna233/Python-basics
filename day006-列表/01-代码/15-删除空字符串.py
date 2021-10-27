# 删除列表里的空字符串
words = ['hello','','','world','ahhh','good','']

# 在使用for...in循环遍历列表时，最好不要对元素进行增删操作
# for word in words:
#     if word == '' :
#         words.remove(word)
# print(words) # ['hello', 'world', 'ahhh', 'good']

i = 0
while i < len(words):
    if words[i] == '':
        words.remove(words[i])
        i -= 1
    i += 1
print(words)

# 可以创建一个新的字符串