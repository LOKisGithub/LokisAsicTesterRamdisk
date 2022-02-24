#!/bin/sh
echo "["
ls -1 /mnt/card/testtool/|awk '{print "\""$1"\",";}'
cat /mnt/card/currentTestTool|awk '{print "\""$1"\"";}'
echo "]"
