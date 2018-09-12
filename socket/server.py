import socket
import time
#udp 使用的是DGRAM tcp使用的是STREAM
def tcp_srv():
    skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr=('127.0.0.1',8998)
    skt.bind(addr)
    skt.listen()

    while 1:
        skt, addr = skt.accept()
        msg=skt.recv(500)
        msg.decode()
        rst=("receiving msg {} from {}".format(msg.decode(),addr))
        print(rst)
        skt.send(rst.encode())


if __name__=="__main__":
    tcp_srv()
