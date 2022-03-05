#!/bin/sh
. ./cgi_lib.cgi
error=false

IFS="&"
set -- $QUERY_STRING

for i in $@; do 
	IFS="="
	set -- $i
	if [ "$1" = "" ] ; then
		# error, all fields are mandatory
		error=true
		invalid_parameter=$1
		break
	else
		if [ "$1" = "selectBoot" ] ; then
			selectedBoot=`urldecode $2`
		fi
	fi
done

show_msg "Updating FW"
sleep 1

/mnt/card/scripts/changeBoot.sh $selectedBoot

cp /tmp/tester.log /mnt/card/logs/

sync

reboot
