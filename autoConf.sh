#!/bin/bash

FIP() {
	TEST="`/sbin/ifconfig eth0 | awk '/inet/ { print $2 }' | sed -e s/addr://`"
	if [ "$TEST" = "" ]; then
		TEST="`/sbin/ifconfig wlan0 | awk '/inet/ { print $2 }' | sed -e s/addr://`"
	fi
}

FIP

if [ "$TEST" = "" ]
	then
	echo "No internet "
#	exit 1
fi

RUNUSER=`id -nu`

if [ "$RUNUSER" != "root" ]
    then
    echo "This program must be executed as root"
    exit 1
fi

echo "Installing some utilities\n"

echo "Installing MEDIBUNTU"

wget http://www.medibuntu.org/sources.list.d/`lsb_release -cs`.list --output-document=/etc/apt/sources.list.d/medibuntu.list

wget -q http://packages.medibuntu.org/medibuntu-key.gpg -O- | sudo apt-key add -

wget http://launchpad.net/ubuntu-tweak/0.5.x/0.5.4.1/+download/ubuntu-tweak_0.5.4.1-1_all.deb
dpkg -i ubuntu-tweak_0.5.4.1-1_all.deb
rm ubuntu-tweak_0.5.4.1-1_all.deb

aptitude update

aptitude -y install w32codecs subversion vim unrar nautilus-open-terminal msttcorefonts build-essential 

aptitude -y install gnome-do pidgin google-chrome-unstable nautilus-dropbox banshee banshee-extension-appindicator synergy openssh-server 

aptitude -y install texlive-latex-extra texmaker

aptitude -y purge gnome-games indicator-messages empathy gwibber

#changing user for configurations to be set by him
su pma

gconftool-2 --type string --set /desktop/gnome/interface/font_name "Sans 8"

gconftool-2 --type string --set /desktop/gnome/interface/document_font_name "Sans 8"

gconftool-2 --type string --set /apps/nautilus/preferences/monospace_font_name "Sans 8"

echo "Environment Fonts Set!\n"
gconftool-2 -s -t int /desktop/gnome/peripherals/keyboard/rate 20

gconftool-2 -s -t int /desktop/gnome/peripherals/keyboard/delay 190

echo "Keyboard Set!\n"

echo "DONE!" 
