# 去重排序
nums = [4, 9, 1, 2, 5, 1, 5, 2, 1, 7, 3, 8, 6, 7]
x = set(nums)
print(x)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
y = list(x)
print(y)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
y.sort(reverse=True)
print(y)  # [9, 8, 7, 6, 5, 4, 3, 2, 1]
