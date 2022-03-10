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
		if [ "$1" = "chkAutotest" ] ; then
			doAutotest=`urldecode $2`
		fi
	fi
done

if [ "$doAutotest" = "true" ] ; then
   echo 1 > /sys/class/gpio/gpio943/active_low
else
   echo 0 > /sys/class/gpio/gpio943/active_low
fi 
