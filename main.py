import socket

HOST_IP = "localhost"
PORT = 5605
addr = (HOST_IP, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)
sock.listen(5)

while True:
    user_sock, user_addr = sock.accept()
    print(repr(user_sock), repr(user_addr))
    data = user_sock.recv(1024)
    print(bytes.decode(data))