import threading
import time

glb_list = [11, 22]
glb_num = 100


def fun1(temp):
    # global glb_num
    # glb_num += 100
    temp.append(33)
    print("---in fun1---%s" % str(temp))


def fun2(temp):
    print("---in fun2---%s" % str(temp))


def main():
    t1 = threading.Thread(target=fun1, args=(glb_list, ))
    t2 = threading.Thread(target=fun2, args=(glb_list, ))

    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)


if __name__ == "__main__":
    main()

