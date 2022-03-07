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
		if [ "$1" = "selectChain" ] ; then
			selectedChain=`urldecode $2`
		fi
	fi
done


/mnt/card/scripts/eeprom_dump.sh $selectedChain

