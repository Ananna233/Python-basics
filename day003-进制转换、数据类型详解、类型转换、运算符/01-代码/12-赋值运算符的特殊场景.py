# 等号链接变量可以传递赋值
a = b = c = d = 'hello'
print(a,b,c,d) # hello hello hello hello

m,n = 3,5  #拆包
print(m,n) # 3,5

x = 'hello','good','yes'
print(x) #('hello', 'good', 'yes')

# 拆包时变量的个数和值的个数不一致时，会报错
# y,z = 1,2,3,4,5
# print(y,z)
# o,p,q = 4,2
# print(o,p,q)

r,*s,t = 1,2,3,4,5,6 # *是可变长度
print(r,s,t) # 1 [2, 3, 4, 5] 6

*r,s,t = 1,2,3,4,5,6
print(r,s,t) # [1, 2, 3, 4] 5 6
