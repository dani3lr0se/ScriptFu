#!/usr/bin/python3

# ScapyScanner tutorial with Cristi Vlad
# SYN Scans

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import sys
from scapy.all import *

if len(sys.argv) !=4: # python ScapyScanner.py 127.0.0.1 1 100
	print("Usage: %s target startport endport"%(sys.argv[0]))
	sys.exit(0)

target = str(sys.argv[1])
startport = int(sys.argv[2])
endport = int(sys.argv[3])
print('Scanning ' +target+' for open TCP port\n')

if startport == endport:
	endport+=1

for x in range(startport, endport):
	packet = IP(dst = target)/TCP(dst = x,flag='S') # SYN
	response = sr1(packet,timeout=0.5,verbose=0)
	if response.haslayer(TCP) and response.getlayer(TCP).flag==0x12: # SYN ACK
		print('Port '+str(x)+' is open!')
	sr(IP(dst=target)/TCP(dport=response.sport,flag='R'),timeout=0.5,verbose=0) # RST

print('Scan is complete!\n')