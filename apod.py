#!/usr/bin/env python3

# Attempts to mimic apod.sh

import urllib
import sys
import os
from bs4 import BeautifulSoup

# Retrieve webpage
filename = "x" # filename = tmp stopped working for some reason? tmp was dir???
urllib.request.urlretrieve("http://apod.nasa.gov/apod/astropix.html", filename)

f = open(filename, "r")
data = [line for line in f]
soup = BeautifulSoup(''.join(data), "html5lib")
os.remove(filename)

try:
    src = soup.body.find_all("a")[1].img["src"]
    if not src:
        sys.exit()
except:
    sys.exit()

# Found the line in which the name is. Extract it
location = "http://apod.nasa.gov/apod/" + src
file_name = src.split("/")[-1]

# image directory
image_dir = os.path.realpath(__file__).rsplit("/", 1)[0] + "/images/"

# If we do not have the image, get it.
if file_name not in os.listdir(image_dir):
    urllib.request.urlretrieve(location, image_dir + file_name)

# set images as background
image = "file://" + image_dir + file_name

command = "DISPLAY=:0 GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.background picture-uri " + image
os.system(command)
command = "DISPLAY=:0 GSETTINGS_BACEND=dconf gsettings set org.gnome.desktop.background picture-options stretched"
os.system(command)
