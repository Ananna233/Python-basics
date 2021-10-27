# 下标 又称为索引，表示第几个数据
# 可迭代对象：str list tuple dict set range 都可以遍历
# str list(列表) tuple(元组) 可以通过下标来获取或者操作数据

# 在计算机里，下标都是从0开始的
wold = 'zhangsan' # 字符串
# 可以通过下标来获取或者修改指定位置的数据
print(wold[4]) # g
# 字符串是不可变的数据类型
# 对字符串的任何操作，都不会改变原有的字符串！
# wold[4] = 'a'

# 切片就是从字符串里复制一段指定的内容，生成一个新的字符串
m = 'abcdefghijklmnopqrstuvwxyz'
print(m[9]) # m[index] ==> 获取指定下标上的数据
# 切片语法 m[start:end:step]
# 包含start 不包含end
# step 指的是步长，间隔，  每隔step-1个 取一次
# step 为负数表示从右往左取

print(m[1:3]) # bc 包含start 不包含end

# 如果只设置了start ，会从start开始“截取”到最后
print(m[3:])  # defghijklmnopqrstuvwxyz

# 如果只设置了end 会从头“截取”到end （不包含end）
print(m[:9])  # abcdefghi

#
print(m[3:15:2]) # dfhjln
print(m[3:15:1]) # defghijklmno 步长默认为1
print('---------------------')

# 正数是从左到右数，当步长是负数，就是从右往左数
print(m[15:3:-1]) # ponmlkjihgfe  包含p 不包含d

print(m[::])   # abcdefghijklmnopqrstuvwxyz 从头到尾复制
print(m[::-1]) # zyxwvutsrqponmlkjihgfedcba 从尾到头复制

# start 和 end 如果为负数 表示从右边数第几个到第几个，，，，最右边的是-1
print(m[-9:-2]) # rstuvwx