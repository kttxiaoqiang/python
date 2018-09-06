'''
sever端流程
1.建立socket socket是负责具体通信的一个实例
2.绑定，为创建的socket指派固定的端口和ip地址
3.接受对方发送的内容
4.给对方发送反馈，此步骤不是必要步骤
'''


#模拟服务器的函数
import socket
def serverFunc():
    #1.建立socket
    #socket.AF_INET 使用ipv4协议族
    #socket.SOCK_DGRAM:使用UDP通信
    skt=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #2.绑定ip和port
    #7852随手指定的端口号
    #地址是一个tuple类型，（ip，port）
    addr=("127.0.0.1",7852)
    skt.bind(addr)

    #接受对方消息
    #等待对方方式为死等，没有其他可能性
    #recvfrom接受的返回值是一个tuple，前一项表示数据，后一项表示地址
    #参数的含义是缓冲区
    #rst=sock.recvfrom(500)
    data,addr=skt.recvfrom(500)
    print(data)
    print(type(data))
    #decode的默认参数是utf-8
    text=data.decode()
    print(type(text))
    print(text)

    #给对方的反馈的小心
    rsp="i am not hungry"

    #发送的数据需要编码成bytes格式
    data=rsp.encode()
    skt.sendto(data,addr)

if __name__=="__main__":
    print("Start severing........")
    serverFunc()
    print("END severing........")