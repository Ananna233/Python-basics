# try...except 语句用来处理程序运行过程中的异常

try:
    print(1 / 0)
    file = open('ddd.txt')
    print(file.read())
    file.close()

# except Exception as e:  # 给异常起来一个变量名e
#     print(e)

# 或者
# except:
#     print('出错了')

# 或者指定出错类型
except (FileNotFoundError, ZeroDivisionError) as e:  # 处理指定类型的异常
    print(e)

# Exception是(FileNotFoundError这些错误的父类