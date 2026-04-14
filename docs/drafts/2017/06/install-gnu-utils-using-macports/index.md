---
title: Install GNU Utils Using MacPorts
created: 2017-06-22 12:32:25
date: 2026-04-13 22:07:51.183434
authors:
  - bendu
label: install-gnu-utils-using-macports
license: CC-BY-4.0
tags:
  - Mac
  - macOS
  - MacPorts
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Configuration

Run the following command after installation.

```
export PATH=/opt/local/libexec/gnubin：/opt/local/bin:/opt/local/sbin:$PATH
export MANPATH=/opt/local/share/man:$MANPATH
```

## Installation

```
sudo port install file
sudo port install coreutils
```

## Issues

1. had issues to sync ports in office, not sure this is due to network issue or firewall in office
   rsync: failed to connect to rsync.macports.org: No route to host (65)
   exit code 10
