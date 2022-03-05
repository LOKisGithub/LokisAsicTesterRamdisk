#!/bin/sh

dd if=/dev/zero of=/dev/mmcblk0 bs=512 count=1
echo "n
p
1


t
b
w
q"|fdisk /dev/mmcblk0
