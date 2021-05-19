# chat-client.py

import socket
import threading
import sys

SERVER_IP = 'localhost'  # Your IP Server
PORT = 7500
BufferSize = 4096




def server_handler(client):
    while True:
        try:
            data = client.recv(BufferSize) # Data form server
        except:
            print('Error~!')
            break

        if (not data) or (data.decode('utf-8') == 'q'):
            print("OUT")
            break
        

        print('User: ', data.decode('utf-8'))
    
    client.close()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


try:
    client.connect((SERVER_IP, PORT))
except:
    print('Error~!')
    sys.exit()



task = threading.Thread(target=server_handler, args=(client,))
task.start()

while True:
    msg = input('Enter Message: ')
    client.sendall(msg.encode('utf-8'))
    if msg == 'q':
        break

client.close()