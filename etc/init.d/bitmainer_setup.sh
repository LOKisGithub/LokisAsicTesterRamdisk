#!/bin/sh
#####################debug###
echo "check mounted config"

#phy_ok=`dmesg | grep "davinci_mdio 4a101000.mdio: phy\[0\]: device 4a101000.mdio:00" | wc -l`
#if [ $phy_ok -eq 1 ];then
#    echo "PHY OK" > /tmp/PHY_STATS
#else
#    echo "PHT ERR" > /tmp/PHY_STATS
#    sleep 5s
#    reboot
#fi


check0p3=`cat /etc/mtab | grep "mtdblock2"`
if [ ""x = "$check0p3"x ] ; then
	echo "mounting config" | tee -a /var/log/messages
	mount -t jffs2 /dev/mtdblock2 /config/
else
	echo "Can't mount /config" | tee -a /var/log/messages
fi

###########################
# dropbear
NO_START=0

if [ ! -f /config/dropbear ] ; then
    echo NO_START=0 > /config/dropbear
fi

cp /config/dropbear /etc/default/dropbear

###########################


###########################
# miner.conf
#if [ ! -f /config/asic-freq.config ] ; then
#    cp /etc/asic-freq.config /config/
#fi

# No configuration, create it!
if [ ! -f /config/cgminer.conf ] ; then
    cp /etc/cgminer.conf.factory /config/cgminer.conf
fi
###########################


###########################
# httpdpasswd
if [ ! -f /config/lighttpd-htdigest.user ] ; then
    cp /etc/lighttpd-htdigest.user /config/lighttpd-htdigest.user
fi

# shadow
if [ ! -f /config/shadow ] ; then
    cp -p /etc/shadow.factory /config/shadow
    chmod 0400 /config/shadow
    rm -f /etc/shadow
    ln -s /config/shadow /etc/shadow
else
    rm -f /etc/shadow
    ln -s /config/shadow /etc/shadow
fi
###########################


#user setting
if [ ! -f /config/user_setting ] ; then
    cp /etc/user_setting.factory /config/user_setting
fi
##########################################
/etc/init.d/syslog start
