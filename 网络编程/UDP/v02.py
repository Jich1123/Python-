import socket

def clientFun():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    text = "Hi 你好吗！"
    data = text.encode()

    sock.sendto(data,("127.0.0.1",7582))

    data,addr = sock.recvfrom(200)
    data = data.decode()
    print(data)

if __name__ == "__main__":
    clientFun()