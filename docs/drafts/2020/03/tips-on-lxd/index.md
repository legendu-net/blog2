---
title: Tips on LXD
created: 2020-03-10 11:45:40
date: 2026-04-13 23:15:25.744084
authors:
  - bendu
label: tips-on-lxd
license: CC-BY-4.0
tags:
  - computer science
  - Docker
  - container
  - LXD
  - LXC
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. LXD only works in Linux.
   It is not supported on macOS or Windows.

1. LXD does not require a CPU which supports virtualization.

1. Docker is a more user-friendly alternative to LXD containers
   and multipass is a more user-friendly alternative to LXD virtual machines.
   It is suggested that you use Docker/multipass instead of LXD.

## [Installation](https://ubuntu.com/tutorials/tutorial-setting-up-lxd-1604#2-install-lxd)

```
sudo snap install lxd
gpasswd -a `id -un` lxd
newgrp lxd
```

## [Setup LXD](https://ubuntu.com/tutorials/tutorial-setting-up-lxd-1604#3-setup-lxd)

```
lxd init
```

## [Launch a container](https://ubuntu.com/tutorials/tutorial-setting-up-lxd-1604#4-launch-a-container)

```
lxc list
lxc launch ubuntu:22.04
lxc exec stirring-beagle -- ls -la
lxc exec -t stirring-beagle /bin/bash
```

## Publish LXD Images

https://ubuntu.com/tutorials/create-custom-lxd-images

https://ubuntu.com/blog/publishing-lxd-images

https://medium.com/@tcij1013/lxc-lxd-cheetsheet-effb5389922d

https://github.com/lxc/lxd/issues/6805

[LXDHub](https://lxdhub.xyz/remote/images/images)

## References

- [LXD @ GitHub](https://github.com/lxc/lxd)

- [macOS and "LXD installed and running?" error](https://github.com/lxc/lxd/issues/4015)

- [LXDHub](https://lxdhub.xyz/remote/images/images)

- [NVidia CUDA inside a LXD container](https://ubuntu.com/blog/nvidia-cuda-inside-a-lxd-container)
