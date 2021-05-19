# basic-client.py

from socket import SOL_SOCKET, SO_REUSEADDR, socket

serverIP = 'localhost'
serverPort = 7000
typeEncode = 'utf-8'

while True:
    data = input('Enter Message: ')
    server = socket()
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    server.connect((serverIP, serverPort))
    server.send(data.encode(typeEncode))

    data_server = server.recv(1024).decode(typeEncode)
    print('Data from Server: ', data_server)
    server.close()
    
