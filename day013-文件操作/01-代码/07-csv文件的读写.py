import csv  # 系统内置模块

# 写
file = open('demo.csv', 'w', encoding='utf8', newline='')  # 打开一个文件
w = csv.writer(file)

# w.writerow(['name','age','score','city'])
# w.writerow(['zhangsan','18','95','上海'])
# w.writerow(['lisi','20','90','beijing'])

w.writerows(
    [
        ['name', 'age', 'score', 'city'],
        ['zhangsan', '18', '95', '上海'],
        ['lisi', '20', '90', 'beijing']
    ]
)

file.close()

# 读
file = open('demo.csv', 'r', encoding='utf8', newline='')
r = csv.reader(file)
for data in r:
    print(data)

file.close()
