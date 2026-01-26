---
title: "Format a Flash Drive in a Linux Virtual Machine"
date: 2021-08-02 20:04:52
modified: 2021-08-02 20:04:52
authors:
  - bendu
label: format-a-flash-drive-in-a-linux-virtual-machine
license: CC-BY-4.0
tags:
  - Computer Science
  - software
  - Linux
  - VirtualBox
  - virtual machine
  - flash drive
  - format
  - fdisk
  - mkfs
---
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Install VirtualBox.

2. Create a Ubuntu virtual machine.

3. Install extension package. 

4. enable USB support

5. select the flash drive you want to format to connect to the VM.

6. use linux commands to format the disk. 
    For example, 
    use `fdisk` to manage partition tables on the falsh drive
    and `mkfs.fat`, `mkfs.ext4`, etc to format the flash drive.
