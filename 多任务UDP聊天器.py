# import time
import threading
import socket


def receive_msg(udp_socket):
    while True:
        receive_data = udp_socket.recvfrom(1024)
        content, addr = receive_data
        print("收到：%s\n 来自： %s\n" % (content.decode("gbk"), addr))


def send_msg(udp_socket, ip_addr, port):
    while True:
        content = input("请输入要发送的内容： ")
        udp_socket.sendto(content.encode("gbk"), (ip_addr, port))
        print("发送成功")


def main():

    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    tgt_addr = ("", 30000)
    udp_socket.bind(tgt_addr)

    # 获得对方IP和端口
    ip_addr = input("请输入对方的IP： ")
    port = int(input("请输入端口号： "))

    # 创建进程
    t1 = threading.Thread(target=send_msg, args=(udp_socket, ip_addr, port))
    t2 = threading.Thread(target=receive_msg, args=(udp_socket, ))

    # 启动进程
    t1.start()
    t2.start()

    # udp_socket.close()
    # print("已关闭对话")


if __name__ == "__main__":
    main()

