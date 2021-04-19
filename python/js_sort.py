#!/usr/bin/env python3

import os

# replace "example_log.txt" with an actual log file #

os.system("grep -o '[^/]*\.js' example_log.txt | sort -u")
