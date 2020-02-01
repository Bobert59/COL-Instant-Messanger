import socket

S = socket.socket()

host = 'localhost'
port = 3149

S.connect((host, port))
print(S.recv(1024))
S.close()