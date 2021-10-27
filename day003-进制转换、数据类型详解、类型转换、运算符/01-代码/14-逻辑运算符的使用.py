# 逻辑运算符  逻辑与and  逻辑或or  逻辑非not
# 运算符的优先级 not>and>or

# 逻辑与，全真才真，一个运算数是False，则结果是False
print(2>1 and 5>3) # True
print(3>2 and 5<4 and 1<0)# False

# 逻辑或，只要有真，就真，，，只有所有运算数是False，才是False
print(1>2 or 1<2) # True
print(2<1 or 3>5) # False

# 逻辑非 True 变 False，  False变True
print(not(5>2)) #False