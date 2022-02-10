import socket
HOST = "localhost"
PORT = 5605
addr = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MSG = bytes(input(), 'utf-8')
sock.connect(addr)
sock.sendall(MSG)
