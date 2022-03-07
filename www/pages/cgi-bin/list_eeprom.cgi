#!/bin/sh
echo "["
ls -1 /mnt/card/eeproms/|awk '{print "\""$1"\",";}'
cat /mnt/card/lastEeprom|awk '{print "\""$1"\"";}'
echo "]"
