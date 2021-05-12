#!/usr/bin/python3

# Created with HackerSploit tutorial

import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(str(s.recv(1024))) # can also add .strip() to cleanup output

def main():
    ip = input("Enter the IP: ")
    port = str(input("Enter the port number: "))

main()
