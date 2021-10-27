# p202
def can_play(clock):
    print('最外层函数被调用了,clock = {}'.format(clock))

    def handle_action(fn):
        print('handle_action函数被调用')
        def do_action(name,game):
            if clock<21:
                fn(name,game)
            else:
                print('太晚了，不能玩游戏')
        return do_action

    return handle_action

@can_play(22)  # 装饰器函数带参数
def play_game(name,game):
    print(name+'正在玩'+game)

play_game('zhangsan','王者荣耀')

# 1.调用can_play函数，并将22传递给clock
# 2.还是@can_play 再调用handle_action方法，把play_game传递给fn
# 3.此时再调用play_game其实调用的就是do_action