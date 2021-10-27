nums = [6,9,2,4,3,8,7,1]

# 排序取最大
# nums.sort()
# print(nums[-1])
# # 倒序
# nums.sort(reverse=True)
# print(nums[0])

# 不排序
maxnum = nums[0]
for num in nums:
    if num > maxnum:
        maxnum = num
print(maxnum)

# 求最大数下标
print('最大数的下标是%d'%nums.index(maxnum))