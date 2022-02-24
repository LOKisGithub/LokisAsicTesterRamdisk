#!/bin/sh
echo "["
ls -1 /mnt/card/BOOT/|awk '{print "\""$1"\",";}'
cat /mnt/card/currentBoot|awk '{print "\""$1"\"";}'
echo "]"
