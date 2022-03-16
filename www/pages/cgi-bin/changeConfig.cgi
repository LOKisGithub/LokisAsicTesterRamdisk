#!/bin/sh
. ./cgi_lib.cgi
error=false

IFS="&"
set -- $QUERY_STRING

for i in $@; do 
	IFS="="
	set -- $i
	if [ "$2" = "" ] ; then
		# error, all fields are mandatory
		error=true
		invalid_parameter=$1
		break
	else
		if [ "$1" = "selectCfg" ] ; then
			selectedCfg=`urldecode $2`
		fi
		if [ "$1" = "selectTools" ] ; then
			selectedTool=`urldecode $2`
		fi
	fi
done

show_msg "Updating Config"
sleep 1

/mnt/card/scripts/changeConfig.sh $selectedCfg
/mnt/card/scripts/changeTestTool.sh $selectedTool

/etc/init.d/cgminer.sh restart > /dev/null
