#!/bin/sh
echo "["
ls -1 /mnt/card/configs/|awk '{print "\""$1"\",";}'
cat /mnt/card/currentConfig|awk '{print "\""$1"\"";}'
echo "]"
