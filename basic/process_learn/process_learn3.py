from multiprocessing import Pool
import os, time


def task(name):
    print('sub process %s execute task %s' % (os.getpid(), name))
    # 休眠一秒
    time.sleep(1)


if __name__ == '__main__':
    print('father process %s' % os.getpid())
    pool = Pool(4)
    for i in range(10):
        pool.apply_async(task, args=(i,))
    print('wait all sub process end...')
    pool.close()
    pool.join()
    print('all sub process end...')
