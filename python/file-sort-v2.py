#!/usr/bin/env python3

# Just another method of file sorting

import os

os.system("grep -o '[^/]*\.js' example_log.txt | sort -u") # Change the file name!
