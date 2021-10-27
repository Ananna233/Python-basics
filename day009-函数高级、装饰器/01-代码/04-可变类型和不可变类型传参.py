def test(a):
    print('修改前a的地址 0x%X' % id(a))  # 0x7FFF419816A0
    a = 100
    print('修改后a的地址 0x%X' % id(a))  # 0x7FFF41982300



def demo(nums):
    print('修改前nums的地址 0x%X' % id(nums))  # 0x256F41B8DC0
    nums[0] = 100
    print('修改后nums的地址 0x%X' % id(nums))  # 0x256F41B8DC0


x = 1
print('调用前x的地址 0x%X' % id(x))  # 0x7FFF419816A0
test(x)
print('调用后x的地址 0x%X' % id(x))  # 0x7FFF419816A0
print(x)  # 1
# int是不可变类型，调用函数传入地址a=x a与x指向同一内存空间，a改变值后，因int是不可变的，a会指向新的地址

y = [1,5,6,8,9,2]
print('调用前y的地址 0x%X' % id(y))  # 0x256F41B8DC0
demo(y)
print('调用后y的地址 0x%X' % id(y))  # 0x256F41B8DC0
print(y)  # [100, 5, 6, 8, 9, 2]