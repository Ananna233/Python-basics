# break和continue 在Python 里只能用在循环语句里
#
# break 用来结束整个循环
# continue 用来结束本轮循环，开始下一轮循环

# i = 0
# while i <5:
#     if i == 3:
#         continue  #<<直接调回while  这样会死循环
#     print(i)
#     i += 1

# continue
i = 0
while i <5:
    if i == 3:
        i += 1
        continue  #<<直接调回while
    print(i)   # 0 1 2 4
    i += 1

# break
i = 0
while i <5:
    if i == 3:
        break  #<<直接结束while
    print(i)   # 0 1 2
    i += 1
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

for i in range(1,10):
    for j in range (1,10):
        if j % 3 ==0:
            break
    else:
            print(i,j)