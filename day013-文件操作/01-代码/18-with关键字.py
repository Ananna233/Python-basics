try:
    file = open('01-打开文件.py','r')
except FileNotFoundError:
    print('文件不存在')
else:
    try:
        file.read()
    finally:
        file.close()


try:
    with open('01-打开文件.py','r',encoding='utf-8') as file:
        file.read()  # 不需要再手动的关闭文件
        # with 关键字会帮助 我们关闭文件
except FileNotFoundError:
    print('文件未找到')


# with 我们称之为上下文管理器，很多需要手动关闭的链接
# 比如说文件链接，socket链接，数据库链接，都能使用with关键字自动关闭链接
# with 关键字后面对象，需要实现 __enter__ 和 __exit__魔法方法