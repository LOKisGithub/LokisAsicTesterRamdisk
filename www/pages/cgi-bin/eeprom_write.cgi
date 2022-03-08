#!/bin/sh -e

# POST upload format:
# -----------------------------29995809218093749221856446032^M
# Content-Disposition: form-data; name="file1"; filename="..."^M
# Content-Type: application/octet-stream^M
# ^M    <--------- headers end with empty line
# file contents
# file contents
# file contents
# ^M    <--------- extra empty line
# -----------------------------29995809218093749221856446032--^M

file=/tmp/$$

trap atexit 0

atexit() {
	rm -rf $file
	sync
	if [ ! $ok ]; then
	    print "<h1>Write to eeprom failed</h1>"
	fi
}

CR=`printf '\r'`

IFS="$CR"
read -r delim_line
IFS=""

while read -r line; do
    test x"$line" = x"" && break
    test x"$line" = x"$CR" && break
done
while read -r line; do
    test x"$line" = x"" && break
    test x"$line" = x"$CR" && break
done

rm -rf /tmp/eeprom.bin
cat - > /tmp/eeprom.bin

/mnt/card/utils/xxd.elf /tmp/eeprom.bin

/mnt/card/scripts/eeprom_write.sh 0 /tmp/eeprom.bin

ok=1
