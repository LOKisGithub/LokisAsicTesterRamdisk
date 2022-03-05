#!/bin/sh

rm -rf /tmp/config
mkdir /tmp/config
cp -r /config /tmp/config
flash_erase -j /dev/mtd2 0 0
mount /config
cp -r /tmp/config/* /config

