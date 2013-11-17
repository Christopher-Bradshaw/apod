#!/usr/bin/env python

# Attempts to mimic apod.sh

import urllib
import sys
import os

# Retrieve webpage
urllib.urlretrieve("http://apod.nasa.gov/apod/astropix.html", "tmp")


f = open("tmp", "r")
# Find img
while 1:
	line = f.readline()
	if not line:
		os.remove("tmp")
		sys.exit()
	if "<IMG SRC" in line:
		os.remove("tmp")
		break


# Found the line in which the name is. Extract it
location = "http://apod.nasa.gov/apod/" + line.split("\"")[1]
file_name = (line.split("\"")[1]).split("/")[-1]

# image directory
image_dir = os.path.realpath(__file__).rsplit("/", 1)[0] + "/images/"

# If we do not have the image, get it.
if file_name not in os.listdir(image_dir):
	urllib.urlretrieve(location, image_dir + file_name)

# set images as background

image = "file://" + image_dir + file_name

command = "DISPLAY=:0 GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.background picture-uri " + image

os.system(command)
os.system("DISPLAY=:0 GSETTINGS_BACEND=dconf gsettings set org.gnome.desktop.background picture-options stretched")
