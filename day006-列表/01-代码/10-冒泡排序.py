nums = [5, 67, 32, 1, 579, 36, 98, 12, 15, 31, 9]
print(len(nums))

for i in range(0, len(nums)):  # [ 0,len(nums) )
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print(nums)
# 每一趟比较次数的优化
# 总比较趟数的优化