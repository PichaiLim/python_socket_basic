# basic-server.py

from socket import socket, SOL_SOCKET, SO_REUSEADDR

serverIP = 'localhost'
serverPort = 7000
typeEncode = 'utf-8'

while True:
    server = socket()
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    server.bind((serverIP, serverPort))
    server.listen(5)
    print('Watting for Client \r\t\n')

    client, addr = server.accept()
    print('Connect form: ', str(addr))

    data = client.recv(1024).decode(typeEncode)
    print('Message form client: ', data)
    client.send('We received your Message! '.encode(typeEncode))
    client.close()
