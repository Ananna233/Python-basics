import copy
#
nums = [1,2,3,4,5]
nums1 = nums # 不是深/浅拷贝，是赋值，指向同一个地址，改变会相互影响
nums2 = nums.copy() # 浅复制，两个内容一模一样，但是，不是同一个对象
nums3 = copy.copy(nums) # 和nums.copy()功能一致，都是浅拷贝

# 深拷贝，只能使用copy模块实现
words = ['hello','world',[100,200,300],'good','anan',3]
words1 = words.copy()
words[0] = '你好'
print(words1) # ['hello', 'world', [100, 200, 300], 'good', 'anan', 3]

words[2][0] = 1
print(words1) # ['hello', 'world', [1, 200, 300], 'good', 'anan', 3]
# words1是words的浅拷贝
# 浅拷贝可以认为只拷贝了一层，内层的列表没有拷贝，使用同一块地址

# 深拷贝
words2 = copy.deepcopy(words)
words[2][0] = 1000
print(words2) # ['hello', 'world', [1, 200, 300], 'good', 'anan', 3]
# words2 完全拷贝到另一个地址空间内，不会再受words影响

# www.pythontutor.com    动态展示数据变化