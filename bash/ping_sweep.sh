#!/bin/bash
for x in `seq 1 254` ; do
  ping -c 1 $1.$x

done
