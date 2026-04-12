---
title: Backup Files Using "rsnapshot"
created: 2015-01-22 14:25:22
date: 2026-04-11 22:10:45.096485
authors:
  - bendu
label: backup-files-using-rsnapshot
license: CC-BY-4.0
tags:
  - software
  - rsnapshot
  - backup
  - synchronization
  - rsync
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

To truncate the relative path while backing up using Rsnapshot:

1. Uncomment the line started with `rsync_long_args`.

1. Remove the `--relative` option and add the `--no-relative` option.
