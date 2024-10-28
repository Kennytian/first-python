import socket

sock = socket.socket()

sock.bind(("127.0.0.1", 9051))
sock.listen(5)
while 1:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print("客户端发送的请求信息：\n", data)
    conn.send(b"HTTP/1.1 200 OK\r\ncontent-type:text/plain\r\n\r\n<h1>i am good</h1>")
    conn.close()
