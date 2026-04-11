---
title: Read CPU Temperature in Linux
created: 2012-05-17 11:24:31
date: 2026-04-05 19:42:37.357503
authors:
- bendu
label: read-cpu-temperature-in-linux
license: CC-BY-4.0
tags:
- modprobe
- sensors
- CPU
- Linux
- temperature
---
<img src="http://dclong.github.io/media/computer/hot.jpg" height="200" width="240" align="right"/>

First you have to install package "lm-sensors". 

    :::bash
    sudo apt install lm-sensors

To detect the cpu temperature, type the following command.

    :::bash
    modprobe coretemp
    sensors

For more instructions on this top, 
see [nixCraft](http://www.cyberciti.biz/faq/howto-linux-get-sensors-information/).
