import socket

def serverFun():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    addr = ("127.0.0.1",7582)
    sock.bind(addr)

    data,addr = sock.recvfrom(500)

    print(data)
    print(type(data))

    text = data.decode()
    print(text)
    print(type(text))

    rsp = "My name is Jich!"
    data = rsp.encode()

    sock.sendto(data,addr)

if __name__ == "__main__":
    print("启动服务。。。。。")
    serverFun()
    print("停止服务。。。。。")