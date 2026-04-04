---
title: "Mount Samba on Mac"
created: 2017-08-26 20:18:18
date: 2017-08-26 20:18:18
authors:
  - bendu
label: mount-samba-on-mac
license: CC-BY-4.0
tags:
  - macOS
  - mount
  - SAMBA
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


## GUI

Go -> Connect to Server

smb://path_to_dir

## Command Line

    mount -t smbfs //user@server/sharename share

    mount_smbfs //user@SERVER/folder ./mntpoint
