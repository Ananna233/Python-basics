# p203
use_permission = 6  # 0b0110

# 权限因子
# 用户权限 &权限因子 ！=0
DEL_PERSSION = 8       # 0b1000
READ_PERMISSION = 4   # 0b0100
WRITE_PERMISSION = 2  # 0b0010
EXE_PERMISSION = 1    # 0b0001


def check_permission(x, y):
    # print(x, y)

    def handle_action(fn):
        def do_action():
            if x & y !=0:
                fn()
            else:
                print('没有对应权限')

        return do_action

    return handle_action


@check_permission(use_permission, READ_PERMISSION)
def read():
    print('正在读取内容')


@check_permission(use_permission, WRITE_PERMISSION)
def write():
    print('正在写入内容')


@check_permission(use_permission, EXE_PERMISSION)
def execute():
    print('正在执行内容')

@check_permission(use_permission, DEL_PERSSION)
def delete():
    print('正在删除内容')


read()
write()
execute()
delete()