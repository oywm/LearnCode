# 互斥锁
from threading import Thread, Lock
import time

g_num = 0


def worl1():
    global g_num
    for i in range(1000000):
        lock.acquire()
        g_num += 1
        lock.release()
    print("-----work1----%d" % g_num)


def work2():
    global g_num
    for i in range(1000000):
        lock.acquire()
        g_num += 1
        lock.release()
    print("-----work2----%d" % g_num)


lock = Lock()
t1 = Thread(target=worl1)
t1.start()

t2 = Thread(target=work2)
t2.start()



