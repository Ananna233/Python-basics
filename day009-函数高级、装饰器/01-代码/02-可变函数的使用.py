def add(a, b):
    return a + b

def add_many(item):
    x = 0
    for i in item:
        x += i
    return x

print(add_many((1, 2, 3, 4, 5, 6, 7, 8, 9)))  # 45
print(add_many([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(add_many({1, 2, 3, 4, 5, 6, 7, 8, 9}))
print(add_many(range(1,10)))

# 一次input只能接受一次用户输入
# nums =[]
# while True:
#     num = input('请输入数字，输入exit结束：')
#     if num == 'exit':
#         break
#     else:
#         nums.append(int(num))
# print(nums)
