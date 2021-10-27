# 列表推导式作用是使用简单的语法创建一个列表
# nums = [i for i in range(10)]
# print(nums)

# nums = []
# i = 0
# for i in range(5):
#     nums.append(i)
# print(nums)

x = [i for i in range(10) if i%2 == 0]
print(x)
y = [i for i in range(10) if i%2]
print(y)

if 3:  # 0是False   其他数字是Ture
    print(1111)

# points 是一个列表。这个列表里的元素都是元组
points = [(x,y) for x in range(5,9) for y in range (10,20)]
print(points)