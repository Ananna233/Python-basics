# p205
class Fibonacci(object):
    def __init__(self, n):
        self.n = n
        self.num1 = self.num2 = 1
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.n:
            self.count += 1
            x = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            return x
        else:
            raise StopIteration


# 1,1,2,3,5,8,13,21,34,55,89,144....
f = Fibonacci(18)
for i in f:
    print(i)


# 既然有列表了，为什么还要有生成器呢？

# 占空间，不占时间
nums =[1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584]

# 占时间，不占空间
f = Fibonacci(18)