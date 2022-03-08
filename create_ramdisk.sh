#!/bin/bash

if (($EUID != 0)); then
  if [[ -t 1 ]]; then
    sudo "$0" "$@"
  else
    exec 1>output_file
    gksu "$0 $@"
  fi
  exit
fi

if [ ! -d /mnt/tmp ]; then
	mkdir /mnt/tmp
fi

gunzip ramdisk.image.gz
mount -o loop ramdisk.image /mnt/tmp

cp -r etc /mnt/tmp/
rm -rf /mnt/tmp/www/pages/*
cp -r www /mnt/tmp/
ln -s /tmp/tester.log /mnt/tmp/www/pages/tester.log
ln -s /tmp/eeprom.bin /mnt/tmp/www/pages/eeprom.bin

umount /mnt/tmp
gzip -v9 ramdisk.image
mkimage -A arm -O linux -C gzip -a 0 -e 0 -T ramdisk -n LokisAsicTester -d ramdisk.image.gz uramdisk.image.gz
