# 作业三：
# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。

import time

def timer(func1):
    #处理被装饰函数，带不定长参数
    def decorator(*args,**kwargs):
        #无返回值的函数
        if func1 == None:
            start_time=time.time()
            time.sleep(1)
            func1(*args,**kwargs)
            end_time=time.time()
            print(f'{end_time-start_time-1:5.5f}')
        #又返回值的函数
        else:
            start_time=time.time()
            time.sleep(1)
            ret = func1(*args,**kwargs)
            end_time=time.time()
            print(f'{end_time-start_time-1:5.5f}')
            return ret
    return decorator

@timer
def add(n=2000000):
    result = 0
    for i in range(n):
        result += i
    print(result)

add()

