import re

# 用户名匹配
# 1.用户名只能包含数字、字母和下划线
# 2.不能以数字开头
# 3.长度在6-16位范围
# username = input('请输入用户名:')
# # x = re.match(r'^\D[a-zA-Z0-9_]{5,15}$', username)
# x = re.fullmatch(r'[a-zA-Z_][a-zA-Z0-9_]{5,15}', username)
# if x is None:
#     print('输入不符合规范')
# else:
#     print(x)

# 密码匹配
# 1. 不能包含!@%^&*字符  2.必须以字母开头  3.长度在6-12位
# password = input("请输入密码:")
# y = re.fullmatch(r'[a-zA-Z][^!@$%^&*]{5,11}', password)
# if y is None:
#     print('密码输入不符合规范')
# else:
#     print(y)

# z = []
# try:
#     with open('demo.txt', 'r', encoding='utf-') as file:
#         # while True:
#         #     content = file.readline().strip('\n')
#         #     if not content:
#         #         break
#         #     if re.match(r'^1000phone', content):
#         #         z.append(content)
#         # 另一种方法
#         content = file.read()  # 读出所有内容
#         z = re.findall(r'1000phone.*', content)  # . 除\n 外所有字符
# except FileNotFoundError:
#     print('文件打开失败')
#
# print(z)

# IP地址检测  0.0.0.0~255.255.255.255
# ipaddr = input('请输入一个IP地址:')

ipaddr = '192.1.249.55'
# \d:一位数  [1-9]\d:10~99  [1]\d{2}:100~199  [2][0-4]\d:200-249  [2][5][0-5]:250~255
# (\d|[1-9]\d|[1]\d{2}|[2][0-4]\d|[2][5][0-5])  当成一个整体匹配一次
p = re.fullmatch(r'((\d|[1-9]\d|[1]\d{2}|[2][0-4]\d|[2][5][0-5])\.){3}(\d|[1-9]\d|[1]\d{2}|[2][0-4]\d|[2][5][0-5])',
                 ipaddr)
print(p)

# 找到字符串里的数字（包括负数，小数）并求和
q = re.finditer(r'-?(0|[1-9]\d*)(\.\d+)?', '-3.14aaa6.5sadad6 8')
for i in q:
    print(i.group())

