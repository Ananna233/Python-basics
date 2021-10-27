# 使用bool内置类可以将其他数据类型转换成布尔值

print(bool(100))  # 将数字100转换成为布尔值   True
print(bool(-1))   # 将数字-1转换成为布尔值也是 True

print(bool(0))    # False
# 数字里，只有数字0被转换成为布尔值是False，其他数字转换为布尔值都是Ture

print(bool('hello'))  # True
print(bool('False'))  # True
print(bool(''))       # False
print(bool(""))       # False
# 字符串里，只有空字符串 ''  or  "" 可以转换成为False，其他字符串都转换成True

# None 转换为布尔值是False
print(bool(None))  # False
print(bool('None'))# True

print(bool([]))   # False 空列表也是False
print(bool(()))   # False （）空元组布尔值也是False
print(bool({}))   # False  {}空字典布尔值也是False

'''在Python中，只有空字符串''or""、数字0、空字典{}、空列表[]、空元组（）、空集合、空数据None会被转换成为False，
   其他的都会转换成为True
'''
s = set()   #空集合
print(bool(s)) #False


# 在计算机里，True和False用数字1 和0 保存
print(True + 1)  #2
print(False+1)   #1
