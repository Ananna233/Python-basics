import os

file_name = input('请输入一个文件路径：')  # yyy.txt ==> yyy.bak.txt

if os.path.isfile(file_name):
    # 打开旧文件
    old_file = open(file_name, encoding='utf8')

    # yyy.txt ==> yyy.bak.txt
    # names = file_name.rpartition('.')  # ('yyy','.','txt')  切片
    # new_file_name = names[0] + '.bak.' + names[2]

    # 方法2
    names = os.path.splitext(file_name)  # ('xxx', '.txt')
    new_file_name = names[0] + '.bak' + names[1]

    new_file = open(new_file_name, 'w', encoding='utf8')  # 打开一个新文件用于写

    # 把旧文件的数据读取出来写入新的文件
    new_file.write(old_file.read())

    new_file.close()
    old_file.close()
else:
    print('您输入的文件不存在')
