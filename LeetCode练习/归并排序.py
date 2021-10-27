#Merge归并 合并

def Merge(nums:list,low:int,mid:int,high:int):
    pass

def MergeSort(nums:list,low:int,high:int):
    if low<high:
        mid = int((low+high)/2)  #从中间划分
        MergeSort(nums,low,mid)  #对左半部分归并排序
        MergeSort(nums,mid+1,high)  #对右半部分归并排序
        Merge(nums,low,mid,high)  #归并