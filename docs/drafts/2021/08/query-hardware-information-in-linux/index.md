---
title: Query Hardware Information in Linux
created: 2021-08-21 23:05:47
date: 2026-04-13 23:14:59.235046
authors:
  - bendu
label: query-hardware-information-in-linux
license: CC-BY-4.0
tags:
  - computer science
  - OS
  - Linux
  - hardware
  - information
  - query
  - list
  - check
  - osquery
  - hw-probe
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```
sudo lshw -html > hardware.html
```

osquery

[hw-probe](https://github.com/linuxhw/hw-probe)
is a hardware probe tool
which probes for hardware,
check operability and find drivers with the help of
[Linux hardware database](https://linux-hardware.org)
.
