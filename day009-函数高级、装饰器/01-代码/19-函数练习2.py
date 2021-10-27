# 写一个自己的replace函数，将指定字符串中指定的旧字符串转换成指定的新字符串
def my_replace(all_str, old_str, new_str):
    # all_str.split(old_str)  以old_str 切片
    # 再以new_str,连一起
    return new_str.join(all_str.split(old_str))


print(my_replace('ahd,a,sk,j12,3f', ',', '-'))  # ahd-a-sk-j12-3f


# 方法2
# for 循环控制不了i？？？
def my_replace2(all_str, old_str, new_str):
    result = ''
    i = 0
    while i < len(all_str):
        temp = all_str[i:i + len(old_str)]
        if temp == old_str:
            result += new_str
            i += len(old_str)
        else:
            result += all_str[i]
            i += 1
    return result


print(my_replace2('ahd,a,sk,j12,3f', ',', '-'))  # ahd-a-sk-j12-3f
print(my_replace2('hello me hi mi how mi what mi', 'mi', 'tony'))  # hello me hi tony how tony what tony
print('----------------------')


# 写一个自己的max函数，获取指定序列中元素的最大值。如果序列是字典，获取字典值的最大值
def get_max(sqe):
    # if type(sqe) == dict:   # 可以写成
    if isinstance(sqe, dict):  # 看对象sqe是否通过dict类创建出来的实例
        sqe = list(sqe.values())
    m = sqe[0]
    for i in sqe:
        if i > m:
            m = i
    return m


print(get_max([1, 28, 6, 35, 6, 56, 32]))  # 56
print(get_max({'a': 10, 'b': 98, 'c': 15, 'x': 54, 'y': 25, 'z': 60}))  # 98
