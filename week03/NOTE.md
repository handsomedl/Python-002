学习笔记
20200809
###本周学习了线程，进程的一些基础概念，还有阻塞非阻塞，同步异步，这些的关系及含义； 还有了解了一些进程间通讯机制，一些锁的概念
###多进程适合于CPU密集型任务，多进程适合于IO密集型，但缺点都是排查调试难度较高
###有个问题mark一下，后续再来查：
执行成功 ：
def f(x,y):
return x+y
with Pool(processes=4) as pool:
result = pool.apply_async(f, (10,2))
print(result.get(timeout=1))

执行失败 ：
def f(x,y):
return x+y
with Pool(processes=4) as pool:
print(pool.map(f, (2,4)))



