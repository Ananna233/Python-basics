# 一个有序数组，原地删除数组中的重复元素，元素只出现一次，返回删除后的数组长度
# P5

# 双指针算法
def removeNum1(li:list):
    if len(li) == 0:
        return 0
    i = 0
    for j in range(1,len(li)):
        if li[i] != li[j]:
            i = i+1
            # 如果顺序前进，即没有发生重复数字，此时i=j，数组不发生改变；如果出现重复数字，i不会前进，j前进，直到i，j所在数字不再重复，i+1，且li[i]=li[j]
            li[i] = li[j]
    return i + 1



li = [0,1,2,2,3,3,4,4,4,5,5]

print(removeNum1(li))
# print(removeNum2(li))