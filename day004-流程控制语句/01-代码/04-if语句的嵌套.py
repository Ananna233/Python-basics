# if的嵌套
# Python语言使用强制缩进来表示语句之间的结构

ticket = input('是否买票了？Y/N')
if ticket == 'Y':
    print('买票了，可以进站。')
    safe = input('是否通过安检Y/N')
    if safe == 'Y':
        print('安检通过，可以上车')
    else:
        print('未通过安检，不能候车')
else:
    print('未买票，不能进站')