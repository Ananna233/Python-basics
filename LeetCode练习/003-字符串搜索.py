#给定字符串A、B  判断字符串B是否是A的子串

import hashlib

def my_hash(s:str):
    md5 = hashlib.md5()  # 应用MD5算法
    data = s
    md5.update(data.encode('utf-8'))
    return md5.hexdigest()  #返回对应的哈希值

def SearchStr1(A:str,B:str):  #哈希函数法
    n = len(A)
    m = len(B)
    hashB = my_hash(B)
    print(hashB)
    for i in range(0,n-m+1):
        hashA = my_hash(A[i:i+m])
        print(hashA)
        if hashA == hashB:
            return i
    return False

A = 'abcdefgh'
B = 'def'
print(SearchStr1(A,B))

#***********************************
#KMP算法
#KMP算法本质上就是找数组中前后缀匹配的位数，前缀子串从0开始数，后缀子串从-1开始数
def get_next(s:str,next:list):
    next[0] = -1
    i = 0  #i是主串，不会回溯，
    j = -1  #j是匹配串，
    while i < len(s):
        #如果不匹配，j回溯，返回子串中匹配的最大匹配数，即前缀中有多少个可以匹配的
        if j==-1:
            j += 1
            i += 1
        elif s[i] == s[j]:  #当前串，前后缀匹配得上，j是匹配个数，例如说当前j=1，即前后缀匹配数是1，当下一个不匹配的话，j从next[1]=1开始，即第0个是匹配的
            i += 1
            j += 1
            next[j] = j
        else:
            j = next[j]

def KMP(A:str,s:str):
    next = [0 for i in range(len(s))]
    get_next(s,next)
    i,j = 0,0
    while i<len(A) and j<len(s):
        if j == -1 or A[i] == s[j]:
            i += 1
            j += 1
        else:
            j = next[j]  #回溯到合适 位置

    if j == len(s):
        return i-j
    else:
        return -1

A = 'abcdefgh'
B = 'aef'
print(KMP(A,B))