#!/bin/sh
echo "["
ls -1 /mnt/card/devicetree/|awk '{print "\""$1"\",";}'
cat /mnt/card/currentDevicetree|awk '{print "\""$1"\"";}'
echo "]"
