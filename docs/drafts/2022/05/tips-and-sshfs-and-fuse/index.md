---
title: "Tips and sshfs and fuse"
created: 2022-05-04 11:15:45
date: 2022-05-06 14:26:48
authors:
  - bendu
label: tips-and-sshfs-and-fuse
license: CC-BY-4.0
tags:
  - Computer Science
  - programming
  - OS
  - Linux
  - sshfs
  - fuse
  - remote
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. If you want to be able to mount remove Linux filesystem on you computer, 
    you can install sshfs and fuse using the following command. 

        wajig install sshfs fuse

    It is suggested that you add you user name into the fuse group using the following command.

        sudo usermod -aG fuse user_name

    You have to restart your computer to make the action take effect. 