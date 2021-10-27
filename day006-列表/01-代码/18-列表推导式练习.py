# 请写出一段Python 代码实现分组一个list里的元素，比如[1,2,3……100]变成[1,2,3],[4,5,6]...
m = [i for i in range(1,100)]
print(m)

# j=0、3、6、9...

n = [m[j:j+3] for j in range(0,100,3)]
print(n)