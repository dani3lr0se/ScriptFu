#!/usr/bin/env python3

import subprocess
import os
import multiprocessing
import sys

nrange = "123.456.789." # Change the IP!

for i in range(1, 254):
    address = nrange + str(i)
    res = subprocess.call(['ping', '-c', '1', address])
    if res == 0:
        print (address) 
    else:
       pass
