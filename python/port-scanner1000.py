#!/usr/bin/python3

import socket
from termcolor import colored

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Enter the IP you want to scan: ")

def portScanner(port):
    if s.connect_ex((host, port)):
        print(colored("[!!] Port %d is closed" % (port), 'red'))
    else:
        print(colored("[*] Port %d is open" % (port), 'green'))

for port in range(1,1000):
    portScanner(port)
