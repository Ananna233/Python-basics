# 　使用递归求ｎ！　ｎ！＝ｎ*（ｎ-1)!
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


print(factorial(20))  # 2432902008176640000


# 使用递归求斐波那契数列的第n个数字
def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1)

print(fibonacci(8))  # 21