score = float(input('请输入你的成绩：'))

if 60 > score >= 0:
    print('不及格')
elif 80 > score >= 60:
    print('中')
elif 90 > score >=80:
    print('良好')
elif 100 >= score >= 90:
    print('优秀')
else:
    print('输错了')