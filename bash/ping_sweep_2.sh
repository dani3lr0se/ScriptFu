#!/bin/bash
# Script launched with the network portion of IP
# It will then ping each of the host portion of the network
# A list of live hosts will be presented to the user

for x in `seq 1 254` ; do
  ping -c 1 $1.$x

done
