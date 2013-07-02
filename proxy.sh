#!/bin/sh

if [ $# != 1 ]; then 
    echo "Usage: [on|off]"
    exit 127
fi

if [ $1 = "on" ]; then 
    gconftool-2 -s /system/http_proxy/use_http_proxy --type boolean true
    gconftool-2 -s /system/proxy/mode --type string manual
    DIST=$(uname -r | grep fc8)
    if [ "$DIST" != "" ]; then
        if [ -e /etc/yum.conf.proxy ]; then
            echo " "
        else
            echo "Create the file /etc/yum.conf.proxy(copy /etc/yum.conf) with line 'proxy=http://proxy.server.com:port'"
            #sudo cp /etc/yum.conf ~/yum.conf.proxy
            #sudo echo "proxy=http://proxy.uminho.pt:3128" >> ~/yum.conf.proxy
            #sudo cp ~/yum.conf.proxy /etc/
        fi
        sudo cp /etc/yum.conf.proxy /etc/yum.conf
        echo "Changed YUM"
    fi
    echo "System Proxy On"
    exit 0
fi

if [ $1 = "off" ]; then
    gconftool-2 -s /system/http_proxy/use_http_proxy --type boolean false
    gconftool-2 -s /system/proxy/mode --type string none
    DIST=$(uname -r | grep fc8)
    if [ "$DIST" != "" ]; then
        if [ -e /etc/yum.conf.ori ]; then
            echo " "
        else
            sudo cp /etc/yum.conf /etc/yum.conf.ori
        fi
        sudo cp /etc/yum.conf.ori /etc/yum.conf
        echo "Changed YUM"
    fi
    echo "System Proxy Off"
    exit 0
fi

