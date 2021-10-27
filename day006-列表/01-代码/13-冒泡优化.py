nums = [6,5,3,1,8,7,2,4]

# 每一趟走完，大数（小数）就会沉下去（浮起来），第i趟会有i个数据不用再比较
# 如果数据已经有序，就跳出循环，不用再比较
count = 0 # 计数器
i = 0
while i < len(nums) -1: # 外循环控制趟数
    j = 0
    flag = True  # 假设一趟都没有交换，，，既已经有序，不用继续比较
    while j < len(nums)-1-i: # 内循环比较
        count += 1
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            flag = False
        j += 1
    if flag:
        # 走完一趟  仍是True，表示没有交换，既已经有序
        break
    i += 1
print(nums)
print('比较了%d次'%count)