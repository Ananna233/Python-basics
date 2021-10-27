a = 'abc'
print(a,id(a))
a += 'db'
print(a,id(a))
li = [1,2,3,[4,5]]
print(id(li),li)
li.append(99)
print(id(li),li)

# print(help(list))
c =dir()
print(type(c))

for i,element in enumerate(li):
    print(i,element)

dict1 = {"zhangsan":10,"lisi":'aaaaadfasd',"zhaoliu":50}
str1 = "today is a good day today is a bad day today is a nice day"
print(dict1.get('lisi'))
print(dict1.get('aadsf'))

#使用空格切割字符串
list1 = str1.split(" ")
print(list1)

arr = 'abcdefg'
for i,j in enumerate(arr):
    print(i,j)

ss = 'abcde'
print(ss[::-1])
globals()


a = (i for i in range(10))
print(a)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
for j in a:
    print(j)

def a():
    print('aaa')
    p1 = yield '123'
    print('bbb')
    if (p1 == 'hello'):
        print('p1是send传过来的')
    p2= yield '234'
    print(p2)

r = a()
next(r)
r.send('hello')

print(5<<3)
