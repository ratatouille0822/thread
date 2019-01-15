import multiprocessing
import time


def demo1():
    print("这是demo1")
    time.sleep(1)


def demo2():
    print("这是demo2")
    time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=demo1)
    p2 = multiprocessing.Process(target=demo2)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()

