import socket
import time
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
    while True:
        print("启动服务。。。。。")
        try:
            serverFun()
        except Exception as e:
            print(e)
        time.sleep(1)
        print("停止服务。。。。。")