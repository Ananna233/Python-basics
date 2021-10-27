nums = [1,0,0,-1,-2,2]
nums.sort()
print(nums)
print(nums[4])

nums = [[1,2,3],[4,5,6]]
if [1,2,3] not in nums:
    nums += [[2,3,4]]
print(nums)

nums = [-2,-1,-1,1,1,2,2]

class Solution:
    def __init__(self,nums,target):
        self.nums = nums
        self.target = target

    def fourSum(self, nums, target: int):
        l = len(nums)  # 数组长度
        nums.sort()
        sun = []
        for i in range(l - 3):
            for j in range(i+1,l-2):
                for k in range(j+1,l-1):
                    for n in range(k+1,l):
                        if nums[i]+nums[j]+nums[k]+nums[n] == target and [[nums[i],nums[j],nums[k],nums[n]]] not in sun:
                            sun += [[nums[i],nums[j],nums[k],nums[n]]]
        return sun

jjj = Solution.fourSum(nums,0)
print(jjj)