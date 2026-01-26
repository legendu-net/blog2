---
title: "Tips on QEMU"
date: 2021-05-03 10:23:53
modified: 2025-12-17 00:04:21
authors:
  - bendu
label: tips-on-qemu
license: CC-BY-4.0
tags:
  - Computer Science
  - programming
  - QEMU
  - virtual
  - machine
  - mouse control
  - VM
  - KVM
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Control Mouse
https://github.com/uoitdnalab/QEMU-Monitor-Control

[How in QEMU send mouse_move, mouse_button, sendkey via some api](https://stackoverflow.com/questions/33362322/how-in-qemu-send-mouse-move-mouse-button-sendkey-via-some-api)


## Turn on Mouse Cursor

qemu-system-x86_64 -show-cursor -enable-kvm -cdrom ubuntu-14.04.3-desktop-amd64.iso -m 2048

## References 

https://www.qemu.org/

https://github.com/uoitdnalab/QEMU-Monitor-Control
