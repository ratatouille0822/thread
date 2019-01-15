import time
import threading
import socket

ip_addr = ""
port = 0

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tgt_addr = ("", 30000)
udp_socket.bind(tgt_addr)
mutex = threading.Lock()


def receive_msg():

    mutex.acquire()

    receive_data = udp_socket.recvfrom(1024)
    content, addr = receive_data
    print("收到：%s\n 来自： %s\n" % (content.decode("gbk"), addr))

    mutex.release()


def send_msg():

    global ip_addr
    global port

    mutex.acquire()

    if not ip_addr:
        ip_addr = input("请输入对方的IP： ")
    if not port:
        port = int(input("请输入端口号： "))

    content = input("请输入要发送的内容： ")
    udp_socket.sendto(content.encode("gbk"), (ip_addr, port))
    print("发送成功")

    mutex.release()

    return content





def main():
    while True:
        t1 = threading.Thread(target=send_msg)
        t2 = threading.Thread(target=receive_msg)

        t1.start()
        t2.start()

        if send_msg() == "exit":
            break

    udp_socket.close()
    print("已关闭对话")


if __name__ == "__main__":
    main()

