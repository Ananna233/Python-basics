# 遍历：将所有的数据都访问一遍。遍历针对的是可迭代对象
# while循环遍历 / for...in循环遍历
killer = ['李白','兰陵王','韩信','赵云','阿珂','孙悟空']

# for...in 循环的本质就是不断的调用迭代器的next方法查找下一个数据
for k in killer:
    print(k)

i = 0
while i <len(killer):
    print(killer[i])
    i += 1
