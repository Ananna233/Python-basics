# 装饰器结构
# def can_play(fn):
#     def inner():
#         pass
#     return inner
#
# @can_paly

# 开放封闭原则
def can_play(fn):
    def inner(name,game,*args,**kwargs):
        print(args)
        clock = kwargs.get('clock',23)  # 获取clock，默认23
        if clock <= 22:
            fn(name,game)
        else:
            print('太晚了，赶紧睡')
    return inner

@can_play
def play_game(name,game):
    print('{}正在玩{}'.format(name,game))


play_game('张三','王者荣耀',55,m = 'hello')
play_game('lisi','LOL',clock = 20)