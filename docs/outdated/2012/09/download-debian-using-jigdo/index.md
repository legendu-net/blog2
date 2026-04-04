---
title: "Download Debian Using Jigdo"
created: 2012-09-03 19:59:19
date: 2015-02-03 19:59:19
authors:
  - bendu
label: download-debian-using-jigdo
license: CC-BY-4.0
tags:
  - jigdo-lite
  - wget
  - debian image
  - jigdo
  - Linux
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

[Weekly Builds of Debian Testing Image]: http://cdimage.debian.org/cdimage/weekly-builds/amd64/jigdo-dvd/

<img src="http://dclong.github.io/media/linux/debian.png" height="200" width="240" align="right"/>

You can save a lot of time using Jigdo to download Debian image 
especially when you have an old version of the image. 

1. Mount the the old version of the image to a folder that you 
have access to, e.g.,

        sudo mount debian-testing.iso /mnt
        
2. Go to [Weekly Builds of Debian Testing Image][] to copy the link
address of the jigdo file that you want to use. 
The first one is usually what you need. 

3. Run the following command in terminal. 

        jigdo-lite link_to_jigdo_file

You will be asked about old vesions of images that you want to use
to accelerate downloading.
You can type in the path where you mounted the image. 
This process will be repeated until you don't have any more old version 
of CD/DVD images to use. Just press enter to continue and files not 
found in the old versions of images will be fetched throught internet. 
