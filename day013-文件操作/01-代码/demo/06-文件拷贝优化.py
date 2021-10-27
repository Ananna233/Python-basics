import os

file_name = input('请输入一个文件路径：')

if os.path.isfile(file_name):
    old_file = open(file_name,'rb')  # 以二进制读

    names = os.path.splitext(file_name)
    new_file_name = names[0] + '.bak' + names[1]

    new_file = open(new_file_name, 'wb')  # 打开一个新文件 以二进制写

    # 把旧文件的数据读取出来写入新的文件
    while True:  # 建议读一点写一点
        content = old_file.read(1024)  # 1024字节
        new_file.write(content)
        if not content:  # if not ''  ==> 如果 不 空  ==》 不空==not False ==》True  if True   空即是真，执行
            break

    new_file.close()
    old_file.close()
else:
    print('您输入的文件不存在')
