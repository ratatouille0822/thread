import time


def sing():
    for i in range(1, 5):
        time.sleep(1)
        print("唱歌")


def dance():
    for i in range(1, 5):
        time.sleep(1)
        print("跳舞")


def main():
    sing()
    dance()


if __name__ == "__main__":
    main()

