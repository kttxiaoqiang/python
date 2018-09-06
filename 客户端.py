import socket
'''
1.建立通信的socket
2.发送内容到指定的服务器
3.接受服务器给定的反馈内容
'''
def clientFunc():
    skt=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    text='i love python'
    #发送的数据是bytes格式
    data=text.encode()

    #发送
    skt.sendto(data,("127.0.0.1",7852))

    data,addr=skt.recvfrom(200)
    data=data.decode()
    print(data)

if __name__=="__main__":
    clientFunc()

