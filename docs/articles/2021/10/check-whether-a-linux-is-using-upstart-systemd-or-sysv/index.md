---
title: Check Whether a Linux Is Using upstart, systemd or SysV
created: 2021-10-05 11:43:26
date: 2026-04-13 23:14:10.352207
authors:
  - bendu
label: check-whether-a-linux-is-using-upstart-systemd-or-sysv
license: CC-BY-4.0
tags:
  - computer science
  - OS
  - Linux
  - systemd
  - upstart
  - SysV
---

The simplest way to check whether a Linux system is running systemd, upstart or SysV
is by running the following command.

```bash
ps -p1 | grep "init\|upstart\|systemd"
```

## References

[How to determine which system manager is running on Linux System](https://www.2daygeek.com/how-to-determine-which-init-system-manager-is-running-on-linux-system/)

[How to know if I am using systemd on Linux?](https://superuser.com/questions/1017959/how-to-know-if-i-am-using-systemd-on-linux)
