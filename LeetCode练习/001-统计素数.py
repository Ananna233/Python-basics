# 统计n内所有素数
def is_Prime(n:int):
    if n == 2 or n == 3:
        return True
    for i in range(2 ,int(pow(n,0.5))+1):  # int 是向下取整的
        if n % i == 0:
            return False
    return True

# 暴力法
def statistics1(n:int):
    ans = 0
    for i in range(2,n+1):
        if is_Prime(i):
            ans += 1
    return ans

# 诶筛法
def statistics2(n:int):
    ans = 0
    li = [1 for i in range(n+1)]  # 初始化为1，默认为素数  直接用下标表示数字
    for i in range(2,n+1):  # 第二个到第n个
        if li[i]:  # 如果记录是素数，检测
            if is_Prime(i):
                ans += 1
                for j in range(i,int(n/i)):  # 检测结果为素数，ans+1，同时把范围内素数i的倍数标注为合数，即li【】=0
                    li[i*j] = 0
    return ans


n = 100000
print(statistics1(n))  # 暴力法
print(statistics2(n))  # 诶筛法
