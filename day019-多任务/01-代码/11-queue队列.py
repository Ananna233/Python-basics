# 1-20.10
import multiprocessing

#
# q1 = multiprocessing.Queue()  # 进程间通讯
# q2 = queue.Queue()  # 线程间通讯

# q创建队列时，可以指定最大长度。默认值是0，表示不限
q = multiprocessing.Queue(5)

q.put('hello')
q.put('hi')
q.put('yes')
q.put('no')
q.put('true')

# print(q.full())  # True 判断是否满了
# q.put('why')  # 无法放进去

# block = True: 表示是阻塞，如果队列已经满了，就等待    False 是不等待
# timeout 超时，等待多久以后程序会报错，单位是秒
# q.put('how',block=False,timeout=5)

# q.put_nowait('how')  # 等价于 q.put('how',block=False)

print(q.get())  # hello  # 先进先出
print(q.get())  # hi
print(q.get())  # yes
print(q.get())  # no
print(q.get())  # true

# q.get()  也是阻塞的方法
# q.get(block=True, timeout=5)
# q.get_nowait()

