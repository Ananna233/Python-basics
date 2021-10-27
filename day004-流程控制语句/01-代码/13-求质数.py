# 求2-200间的所有质数

# for……in 法
# for i in range(2,201):
#     flat = 0
#     for j in range(2,int(i**0.5)+1):
#         if i % j ==0:
#             flat = 1
#             break
#     if flat ==0:
#         print(i,"是质数")

# if……else
# for i in range(2,201):
#     for j in range(2,int(i**0.5)+1):
#         if i % j==0:
#             break
#     else :  # 当 if i%j==0 执行过if语句后，else就不会再执行，，只有最后一次没有执行过if才会执行else
#         print (i,"是质数")

# 假设成立法
# for i in range(2,201):
#     flag = True
#     for  j in range(2,int(i**0.5)+1):
#         if i % j == 0:
#             flag = False
#             break
#     if flag :
#         print (i,'是质数')

# 计数法
for i in range(2,201):
    count = 0 # 假设可以被n个数字整除
    for j in range(2,i):
        if i % j ==0:
            count += 1
    if count == 0:
        print(i,'是质数')
    else:
        print(i,'是合数，可以被',count,'个整数整除')

