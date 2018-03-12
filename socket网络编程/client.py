from socket import *

HOST = '192.168.1.105'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input("Client>")
    data = str.encode(data)
    if not data:
        break
    tcpCliSock.send(data)
    message = tcpCliSock.recv(BUFSIZ)
    message = bytes.decode(message)
    if not data:
        break
    print ("="*20)
    print ("[From Server]:",message)

tcpCliSock.close()

