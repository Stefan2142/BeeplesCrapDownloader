# BeeplesCrapDownloader
Script used for automatic download of images from a Instagram account of awesome CGI and VFX artist [Beeple](http://www.beeple-crap.com/) who is publishing an artwork per day for over ten years now.

# Requirements
Script is tested on Python 2.7.x and requires external library [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/). 

# Usage
This code is meant to be used with Windows's own task scheduling platform. A scheduled task should be created to run this script at each startup of system (this implies that user is shutting down his pc each day and turning it on the next one). 

# Things to do:
- Add logic for checking if the latest image is the same as the current desktop (meaning user didnt shut his pc down)
- Add option for saving previous images in a 'old' folder

# Important notice
Script is made for fun and in my spare time for my own needs. So it works as it works. However, I do intend in future to polish the code and implement a better functionality to this project
