import socket
skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('127.0.0.1', 12345)
# skt.bind(addr)
skt.close()