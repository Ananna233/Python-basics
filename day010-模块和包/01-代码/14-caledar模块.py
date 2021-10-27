import calendar  # 日历模块

calendar.setfirstweekday((calendar.SUNDAY))  # 设置每周起始日期码（这里是SUNDAY），周一到周日分别对应0~6
print(calendar.firstweekday())  # 返回当前每周起始日期的设置。默认情况下，首次载入calendar模块时返回0，即星期一

c = calendar.calendar(2019)  # 生成2019年的日历，并且以周日为其实日期码
print(c) # 打印2019年日历

print(calendar.isleap(2020))  # True  闰年返回True，否则返回False
count = calendar.leapdays(1988,2012)  # 获取1988~2012 一共有多少个闰年
print(calendar.month(2019, 3))  # 打印2019年3月的日历

# 用处不大