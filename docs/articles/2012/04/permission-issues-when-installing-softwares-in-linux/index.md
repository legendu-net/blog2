---
title: Permission Issues when Installing Softwares in Linux
created: 2012-04-30 00:00:00
date: 2026-04-05 19:42:37.367444
authors:
- bendu
label: permission-issues-when-installing-softwares-in-linux
license: CC-BY-4.0
tags:
- Linux
- softwares
- permission
- issue
- chmod
---
Sometime when you install softwares in Linux, 
you get an error message saying that you do not have permission while you used sudo or the root account. 
This probably means that you do not have full access to some installation files.
An easy way to solve this problem is to change file permissions of these installation files.
For example, 
suppose "inst" is the directory containing installation files, 
you can 
change file access use the following command and try installation again.

    chmod -R 755 inst

