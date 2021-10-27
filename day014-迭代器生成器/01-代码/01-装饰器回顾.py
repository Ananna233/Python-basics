# p202
def can_play(fn):
    print('外部函数被调用了')

    def inner(name, game, **kwargs):  # kwargs = {'clock':22}
        clock = kwargs.get('clock', 21)
        if clock >= 21:
            print('太晚了，不能玩游戏')
        else:
            fn(name, game)

    return inner


@can_play
def play_game(name, game):
    print(name + '正在玩' + game)


play_game('zhangsan', '王者荣耀', clock=20)
