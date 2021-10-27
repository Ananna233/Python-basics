import time

print(time.time())  # 获取从1970-01-01 00:00:00 UTC到现在时间的秒数
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 2020-09-27 09:46:48 按照指定格式输出日期
print(time.asctime())  # Sun Sep 27 09:45:32 2020  # 传参  是元组
print(time.ctime())  # Sun Sep 27 09:45:32 2020  #可以给个参数，，，参数是时间戳

print('hello')
print(time.sleep(3))  # 让线程暂停3秒
print('world')