#!/usr/bin/python3

import socket
# 1st method to do this script

# s = socket.socket()

# ip = input("Enter the IP: ")
# port = str(input("Enter the port number: "))

# s.connect((ip, int(port)))

# print(s.recv(1024))

# 2nd method to do this script

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(str(s.recv(1024))) # can also add .strip() to cleanup output

def main():
    ip = input("Enter the IP: ")
    port = str(input("Enter the port number: "))

main()
