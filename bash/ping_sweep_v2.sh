#!/bin/bash

# replace example ip with an actual ip address to be scanned

for i in `seq 1 255`; do ping -c 1 123.456.789.$i | tr \\n ' ' | awk '/1 received/ {print $2}'; done
