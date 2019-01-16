import multiprocessing
import os
import time
import random


def test_pool(num):
    t_start = time.time()
    print("这是第%d次实现" % num)
    print("进程号是%d" % os.getpid())
    time.sleep(1)
    t_stop = time.time()
    t = t_stop - t_start
    print("一共用了%.2f秒" % t)


def main():
    pool = multiprocessing.Pool(3)
    for i in range(10):
        pool.apply_async(test_pool, (i, ))
    print("------------start----------")
    pool.close()
    pool.join()
    print("------------the end----------")


if __name__ == "__main__":
    main()
