#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 444
# binding to socket
serversocket.bind((host, port)) #host will be replaced with IP, if changed and not running on host

# starting TCP listener
serversocket.listen(3)
while True:
    #starting the connection
    clientsocket,address = serversocket.accept()

    print("Received connection from: %s " % str(address))

    message = 'Thank you for connecting to the server.' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
