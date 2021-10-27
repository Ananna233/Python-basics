def ShellSort(nums:list,n:int):  #希尔排序
    d = int(n/2)
    while d >= 1:
        for i in range(d,n):
            temp = nums[i]
            j = i
            while j>=d and nums[j-d] > temp:
                nums[j] = nums[j-d]
                j -= d
            nums[j]  = temp
        d = int(d/2)
    print(nums)

li = [9,2,3,1,10,8,1,5,77]
ShellSort(li,len(li))

#不稳定
#适用性：仅适用于顺序表，不适用于链表
#空间O(0)
#时间平均O(n^1.3)   最坏O(n^2)