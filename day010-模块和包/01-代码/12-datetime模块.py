import datetime as dt

# 以一个下划线_开始  _x
# 一两个下划线__开始  __x
# 以两个下划线开始，再一两个下划线结束  __x__
print(dt.datetime.now())  # 2020-09-27 09:29:48.636379 获取当前时间
print(dt.date(2020, 1, 1))  # 2020-01-01 创建一个时间、
print(dt.time(18, 23, 45))  # 18:23:45 创建一个时间
print(dt.datetime.now() + dt.timedelta(3))  # 2020-09-30 09:35:24.523055 计算3天以后的日期
