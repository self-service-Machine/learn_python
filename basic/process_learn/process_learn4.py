# -*-coding:utf-8-*-
from multiprocessing import Process


def plus():
    print('sub process1 start')
    global g_num
    g_num += 50
    print('g_num is %d' % g_num)
    print('sub process1 end')


def minus():
    print('sub process2 start')
    global g_num
    g_num -= 50
    print('g_num is %d' % g_num)
    print('sub process2 end')


# 定义全局变量
g_num = 100


if __name__ == '__main__':
    print('main process start')
    p1 = Process(target=plus)
    p2 = Process(target=minus)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('main process end')
