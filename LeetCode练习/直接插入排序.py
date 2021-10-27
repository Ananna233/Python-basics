def InsertSort(nums:list,n:int):  #直接插入排序
    for i in range(1,n):  #第一个默认已有序
        if nums[i]<nums[i-1]:  #当前数比前面的数小
            temp = nums[i]  #辅助变量
            j = i-1
            while temp < nums[j] and j >= 0:  #当前nums[j]>temp 都要右移，前提：j>=0
                nums[j+1] = nums[j]  #所有比temp大的都要右移
                j -= 1
            nums[j+1] = temp  #此时j指在，num[j]<temp
    print(nums)

#空间O(1)
#时间O(n^2)
#稳定
li = [9,2,3,1,10,8]
InsertSort(li,len(li))

#优化:折半插入排序
#链表的插入排序