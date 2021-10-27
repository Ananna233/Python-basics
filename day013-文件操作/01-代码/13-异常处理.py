# 在程序运行过程中，由于编码不规范等造成程序无法正常执行，次数程序就会报错
# 健壮性：很多编程语言都有异常处理机制

def div(a, b):
    return a / b

try:
    x = div(5, 0)
    print('ahhaha')
except Exception as e:  # 如果程序出错，会立即跳转到except语句
    print('程序出错了！！！！！！')
else:  # 程序运行如果没有出错，会执行else语句里的代码
    print('计算结果是'+x)
