#!/usr/bin/env python3

filenames = set()

# replace "example_log.txt" with an actual log file #

with open(r"example_log.txt") as f:
    for line in f:
        end = line.rfind(".js") + 3 # 3 = len(".js")
        start = line.rfind("/", 0, end) + 1 # 1 = len("/")
        filename = line[start:end]
        if filename.endswith(".js"):
            filenames.add(filename)


for filename in sorted(filenames, key=str.lower):
    print(filename)
