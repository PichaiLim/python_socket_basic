# chat-server.py

import socket
import datetime
import threading

PORT = 7500
BufferSize = 4096
SERVER_IP = 'localhost' # Your IP

clist = [] # Client List

def client_handler(client, addr):
    while True:
        try:
            data = client.recv(BufferSize)
        except:
            clist.remove(clist);
            break

        if (not data) or (data.decode('utf-8') == 'q'):
            clist.remove(client)
            print('OUT: ', client)
            break

        msg = str(addr) + ' >>>> ' + data.decode('utf-8') #ข้อความส่งไปให้ชาวบ้าน
        print('User: ')
        print('---------')
        
        for c in clist:
            c.snedall(msg.endcode('utf-8'))

    client.close()



 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((SERVER_IP, PORT))
server.listen(5)

while True:
    client, addr = server.accept()
    clist.append(client)
    print('All CLient: ', clist)

    task = threading.Thread(target=client_handler, args=(client, addr))
    task.start()
