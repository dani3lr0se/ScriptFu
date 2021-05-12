#!/usr/bin/env python3

# Simple file sorting script. Customize to fit your needs.

filenames = set()

with open(r"example_log.txt") as f: # Change the file name!
    for line in f:
        end = line.rfind(".js") + 3 # 3 = len(".js")
        start = line.rfind("/", 0, end) + 1 # 1 = len("/")
        filename = line[start:end]
        if filename.endswith(".js"):
            filenames.add(filename)


for filename in sorted(filenames, key=str.lower):
    print(filename)
