import socket
from cryptography import fernet
host = '127.0.0.1'
port = 12900
CS = socket.socket()
CS.connect((host, port))

message = input(">> ")

while message.lower().strip() != 'bye':
    CS.send(message.encode())
    data = CS.recv(1024).decode()
    print(str(data))
    message = input(">> ")
CS.close()
