# uuid用来生成一个全局唯一的id
import uuid

# uuid1 基于MAC地址，时间戳，随机数生成
print(uuid.uuid1())  # 随机生成 32个长度  每一个字符有16个选择  16**32
# print(uuid.uuid2()) 默认不让用

# uuid3和uuid5是使用传入的字符串根据指定的算法算出来的，是固定的
# uuid3基于MD5算法  uuid5基于sha1
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'zhangsan'))  # 生成固定对的uuid
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'zhangsan'))  # 生成固定对的uuid

# 随机 使用最多
# 通过伪随机数  有一定概率重复的
print(uuid.uuid4())