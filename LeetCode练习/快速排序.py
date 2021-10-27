#用第一个元素将待排序序列分为左右两部分
def Partition(nums:list,low:int,high:int):
    pivot = nums[low]  #以第一个元素为枢轴
    while low<high:  #用low 和 high搜索枢轴的最终位置
        while low<high and nums[high]>=pivot:
            high -= 1
        nums[low] = nums[high]  #将比枢轴小的元素移动到左端，即low端
        while low<high and nums[low]<=pivot:
            low += 1
        nums[high] = nums[low]  #将比枢轴大的元素移动到右端，即high端
    nums[low] = pivot  #此时low == high 元素移动完毕，nums[low]是空位
    return low  #返回当前枢纽下标，即枢纽将数组划分为左右两份（左侧<pivot   右侧>pivot)

def QuickSort(nums:list,low:int,high:int):  #快排，low排序数组最左下标，high排序数组最右下标
    if low<high:  #递归结束条件  即最小分区=1
        pivotpos = Partition(nums,low,high)  #划分
        QuickSort(nums,low,pivotpos-1)  #划分左字表
        QuickSort(nums,pivotpos+1,high)  #划分右字表


li = [1111,25,45,35,6,1,38,99,46,33]
QuickSort(li,0,len(li)-1)
print(li)