from cryptography.fernet import Fernet
import socket
host = '127.0.0.1'
port = 12900

SC = socket.socket()
SC.bind((host, port))
SC.listen(2)

conn, address = SC.accept()
print('[*]Connection From: ' + str(address))

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(str(data))
    data = input('>> ')
    conn.send(data.encode())
conn.close()
