import sys

# sys.stdin 接收用户的输入，说白了就是读取键盘里的输入数据
# sys.stdout 标准输出

# sys.stderr 错误输出

s_in = sys.stdin  # input就是读取sys.stdin里的数据

while True:
    content = s_in.readline().rstrip('\n')  # 去掉回车换行符
    if content == '':
        break
    print(content)

sys.stdout = open('stdout.txt', 'w', encoding='utf8')
print('hello')
print('world')

sys.stderr = open('stderr.txt', 'w', encoding='utf-8')
