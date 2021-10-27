# 列表可以使用extend方法将两个列表合并成为一个列表
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9]
nums1.extend(nums2)
print(nums1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

person1 = {'name': 'zhangsan', 'age': 20}
person2 = {'addr': 'shanghai', 'height': 181}
person1.update(person2)
print(person1)  # {'name': 'zhangsan', 'age': 20, 'addr': 'shanghai', 'height': 181}

# 列表list  元组tuple 字符串str 可以通过加法运算合并成一个新的字符串
# 字典不可以使用加法运算，会报错
print(nums1 + nums2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 7, 8, 9]
words1 = ('hello', 'world')
words2 = ('hi', 'ok')
print(words2 + words1)  # ('hi', 'ok', 'hello', 'world')
a = 'str'
b = 'ing'
print(a + b)  # string
