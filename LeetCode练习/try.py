alist = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
print(len(alist))
lst2 = sum(alist,[])
print(lst2)
a = lambda x,y,z,r:x+y+z+r
print(a(1,20,300,4000))

li = [0,5,-8,-3,5,3,9,10,-11]
res = sorted(li,key=lambda x:(x<0,abs(x)))
print(res)

#过滤器
res2 = list(filter(lambda x:x%2==0,li))
print(res2)

aj = 'abcabcabc'
akk = aj.split('abcd')
print(akk)

#索引为单数
al = [1,2,3,4,5,6,7,8,9]
# al_list = [y[1] for y in filter(lambda x:x[0]%2==1, ( (i,al[i]) for i in range(len(al)) ) )]
al_list = [al[y] for y in filter(lambda x:x%2==1, ( (i) for i in range(len(al)) ) ) ]
print(al_list)


person = {
    'name':'zhangsan',
    'age':23,
    'height':172
}
for i in person:
    print(i)

tuples = (1,2,3,4,5,6,7)
for i in tuples:
    print(i)