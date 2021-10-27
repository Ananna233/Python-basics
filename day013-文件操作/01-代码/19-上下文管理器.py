# p200
# with 语句后面的结果对象，需要重写 __enter__和 __exit__方法
# 当进入with代码模块 时，会自动 调用__enter__方法里的代码
# 当with代码模块执行完成以后，会自动调用__exit__方法


class Demo():
    def __enter__(self):
        print('__enter__方法被执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__方法被调用了')


def create_obj():
    x = Demo()
    return x

#d = create_obj().__enter__()
with create_obj() as d:  # as 变量名
    # 变量d 不是create_obj的返回结果
    # 它是创建对象x调用__enter__之后返回的结果
    print(d)