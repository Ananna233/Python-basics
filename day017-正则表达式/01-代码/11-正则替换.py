# 正则表达式作用就是用来对字符串进行检索和替换
# 检索: match  search  fullmacth  finditer  findall
# 替换: sub

import re

t = 'afakf23afr5rges6654s5'

# re.sub(匹配规则, '替换内容' ,原字符串)
print(re.sub(r'\d', 'x', t))  # afakfxxafrxrgesxxxxsx
print(re.sub(r'\d+', 'x', t))  # afakfxafrxrgesxsx

p = 'hello34good56'  # 把字符串里的数字 *2 hello68good112

# 第一个参数是 正则表达式
# 第二个参数是 新字符或者一个函数
# 第三个参数是 需要被替换的原来的字符串

def test(x):
    y = int(x.group(0))
    y *= 2
    return str(y)

# sub内部在调用 test方法时，会把每一个匹配到死亡数据以re.Match的格式传参
print(re.sub(r'\d+',test,p))  # test函数是自动调用的  hello68good112
