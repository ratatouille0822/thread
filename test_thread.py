import time
import threading as th


def sing():
    for i in range(1, 5):
        time.sleep(1)
        print("唱歌")


def dance():
    for i in range(1, 5):
        time.sleep(1)
        print("跳舞")


def main():
    t1 = th.Thread(target=sing)
    t2 = th.Thread(target=dance)
    t1.start()
    t2.start()

    # sing()
    # dance()


if __name__ == "__main__":
    main()

