from multiprocessing import Process


# 执行子进程
def test(inteval):
    print("I'm child process")


# 主进程
def main():
    print('main process start')
    # 实例化Process进程类
    p = Process(target=test, args=(1,))
    p.start()
    print('main process end')


if __name__ == "__main__":
    main()
