#!/bin/bash

# 7/1/2013
# Grabs the latest APOD image and sets it as the wallpaper.
# Should be run hourly/daily with cron

# This is to let it run with cron
#########################################
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/home/christopher/.local/bin:/home/christopher/bin
export DISPLAY=:0.0
########################################

#exec >/dev/null 2>&1

# Run every 24 hours

# Download apod picture (store in ./images) and set as background

DIR=`dirname $0`

wget -P $DIR http://apod.nasa.gov/apod/astropix.html

NAME=`cat $DIR/astropix.html | grep "<IMG SRC=" | cut -d'"' -f2`

rm $DIR/astropix.html
# 0 found, 1 not.
# exits if there is no jpg
grep -q .jpg <(echo $NAME)

if [ $? -ne 0 ]
	then 
	exit
fi


NAME="http://apod.nasa.gov/apod/"$NAME


wget -nc -P $DIR/images/ $NAME 


if [ $? -eq 0 ] 
	then

	NAME=`echo $NAME | cut -d'/' -f7`

	gsettings set org.gnome.desktop.background picture-uri file:///home/christopher/Programming/apod/images/$NAME
	gsettings set org.gnome.desktop.background picture-options "stretched"
fi
