from multiprocessing import Process
import time
import os


# 继承Process类
class SubProcess(Process):
    def __init__(self, interval, name=''):
        # 调用父类的初始化方法
        Process.__init__(self)
        self.interval = interval
        if name:
            self.name = name

    def run(self):
        print('chile process %s start execute, father process is %s' % (os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_stop = time.time()
        print('chile process %s execute end, time spend %0.2f' % (os.getpid(), t_stop - t_start))


if __name__ == '__main__':
    print('father process start')
    print('father process PID: %s' % os.getpid())
    p1 = SubProcess(interval=1, name='mrsoft')
    p2 = SubProcess(interval=2)

    p1.start()
    p2.start()

    # 输出p1、p2的进程状态，真正执行返回True，否则返回False
    print('p1.is_alive(): %s' % p1.is_alive())
    print('p2.is_alive(): %s' % p2.is_alive())

    print('p1.name: %s; p1.pid: %s' % (p1.name, p1.pid))
    print('p2.name: %s; p2.pid: %s' % (p2.name, p2.pid))

    # 等待子进程
    p1.join()
    p2.join()

    print('father process end')
