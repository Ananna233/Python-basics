class A(object):
    pass


class B(object):
    def foo(self):
        print('我是B类里的foo方法')


class C(A):
    def foo(self):
        print('我是C类里的foo方法')


class D(B):
    pass


class X(D, C):
    pass

x =X()
x.foo()  # 我是B类里的foo方法
print(X.__mro__)  # (<class '__main__.X'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# 继承  找父类 是深度优先
# X(D, C)  向找D  再C

# 结构:  B ==> D ==》X
#       A ==> C ==》X