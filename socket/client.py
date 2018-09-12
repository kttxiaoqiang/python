import socket
def tcp_client():
    skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr = ('127.0.0.1', 8998)
    skt.connect(addr)
    msg='i love python'
    msg=msg.encode()
    skt.send(msg)
    rst=skt.recv(500)
    rst=rst.decode()
    print(rst)
    skt.close()
if __name__=='__main__':
    tcp_client()