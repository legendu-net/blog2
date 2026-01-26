---
title: "Fix Package Installation Issue in Linux"
date: 2018-07-21 12:31:03
modified: 2018-07-21 12:31:03
authors:
  - bendu
label: fix-package-installation-issue-in-linux
license: CC-BY-4.0
tags:
  - Linux
  - package management
  - issue
  - apt
  - dpkg
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Error message: The package hl1440lpr needs to be reinstalled, but I can't find an archive for it.


Steps to fix the issue:

Start with

```
sudo dpkg --remove --force-all hl1440lpr
```

If that fails ...

```
sudo -i
cd /var/lib/dpkg/info
rm -rf hl1440lpr*
dpkg --remove --force-remove-reinstreq hl1440lpr
exit
```

Confirm apt-get is fixed
```
sudo apt-get update
```

## Reference

https://askubuntu.com/questions/88371/apt-synaptic-needs-to-reinstall-package-but-cant-find-the-archive-for-it