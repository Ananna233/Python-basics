# 使用位运算，获取十六进制颜色 0xf0384E 的RGB值，以十进制打印输出
# Red=0xf0  Green=0x38   blue=0x4e
color = 0xF0384e

print(bin(color))

red = color>>16
print(red)

green = color>>8
# print(hex(green))
green = green & 0x00ff  # 按位与& 同为1则1 否则为0
print(hex(green))

blue = color & 0x0000ff

print(hex(blue))