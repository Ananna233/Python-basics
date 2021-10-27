chars = ['a', 'b', 'b', 'v', 'g', 'b', 'a', 's', 't', 'u', 'v', 'd', 's', 'a', 'g']
print(chars.count('a'))
# 统计所有字符出现的次数 可以使用字典
char_count = {}

for char in chars:
    if char not in char_count:
        char_count[char] = chars.count(char)
print(char_count)  # {'a': 3, 'b': 3, 'v': 2, 'g': 2, 's': 2, 't': 1, 'u': 1, 'd': 1}

vs = char_count.values()
# 可以使用内置函数max取最大数
max_count = max(vs)

for k, v in char_count.items():
    if v == max_count:
        print(k)  # a b
