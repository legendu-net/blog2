---
title: "Missing Grub Menu of Windows Operating System"
date: 2012-05-03 19:10:47
modified: 2021-09-16 09:29:19
authors:
  - bendu
label: missing-grub-windows
license: CC-BY-4.0
tags:
  - Windows
  - Linux
  - OS
  - Debian
---

I came across this problem after I installed both Debian and Windows 7 system on my laptop.
After searching online, I found a solution to this problem. 
1. Open /etc/default/grub as root user and make sure the following line is somewhere in the file and uncommented:

        GRUB_DISABLE_OS_PROBER=false

2. Run command `update-grub2` and then reboot your computer.

This solution is not just for Windows and Linux dual boot. 
It is also for dual/multiple Linux operating systems boot. 
