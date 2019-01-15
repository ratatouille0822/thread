import time
import threading


glb_num = 100


def demo1(num):
    global glb_num
    mutex.acquire()
    for i in range(num):
        glb_num += 1
    mutex.release()
    print("----demo1 -----%d" % glb_num)


def demo2(num):
    global glb_num
    mutex.acquire()
    for i in range(num):
        glb_num += 1
    mutex.release()
    print("----demo2 -----%d" % glb_num)


mutex = threading.Lock()

def main():
    t1 = threading.Thread(target=demo1, args=(10000000,))
    t2 = threading.Thread(target=demo2, args=(10000000,))

    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)


if __name__ == "__main__":
    main()