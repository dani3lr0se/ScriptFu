#!/usr/bin/python3

# Created with HackerSploit tutorial

import socket

s = socket.socket()

ip = input("Enter the IP: ")
port = str(input("Enter the port number: "))

s.connect((ip, int(port)))

print(s.recv(1024))