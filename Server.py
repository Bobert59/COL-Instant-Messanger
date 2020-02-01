import socket

S = socket.socket()

host = 'localhost'
port = 3149

S.bind((host, port))
S.listen(5)
print((host, port))

while True:
    C, addr = S.accept()
    print('got connection from addr')
    C.send(bytes("Buy a tesla", 'utf-8'))
    C.close()