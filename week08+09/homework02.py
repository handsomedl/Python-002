#作业二：
#自定义一个 python 函数，实现 map() 函数的功能。
#===================================
#返回的是一个可迭代对象
# m = map(square, range(10))

def square(x):
    return x**2

def mymap(func,iter):
    for i in iter:
        yield func(i)


m = mymap(square,range(5))

m.__next__()

next(m)

for i in m:
    print(i)

