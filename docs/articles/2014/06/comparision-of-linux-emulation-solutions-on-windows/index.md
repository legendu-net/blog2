---
title: "Comparision of Linux Emulation Solutions on Windows"
created: 2014-06-13 22:21:09
date: 2021-09-26 21:57:22
authors:
  - bendu
label: comparision-of-linux-emulation-solutions-on-windows
license: CC-BY-4.0
tags:
  - Virtual Machine
  - Cygwin
  - MobaXterm
  - VirtualBox
  - Linux Emulation
---

 
1. Virtual machine based on Virtualbox, etc. is an overkill, 
    generally speaking.
    It provides complete functionalities 
    but is more CPU and memory hangry.

2. WSL 2 is the currently the best solution comes with Windows 10+.
    It is essentially a virtual machine but based on Hyper-V.

3. Cygwin, MobaXterm, etc. are outdated 
    as WSL 2 is an integrated solution in Windows 10+.

[x86 Virtualization in Browser](https://copy.sh/v86/)