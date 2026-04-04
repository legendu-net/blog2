---
title: "Package Management for Debian and Ubuntu"
created: 2025-12-29 19:31:07
date: 2026-01-01 09:01:37
authors:
  - bendu
label: package-management-for-debian-and-ubuntu
license: CC-BY-4.0
tags:
  - Computer Science
  - Linux
  - Debian
  - Ubuntu
  - package
  - management
  - apt
  - get
  - aptitude
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

- dpkg: low-level (without deps manageent)
- `apt-get` (and `apt-*`): low-level (with deps management)
- `apt`: user friendly
- `aptitude`: even more user friendly
- ~~wajig~~: use `apt` or `aptitude` instead

Overall, 
`apt` and `aptitude` are recommended.

## aptitude

`aptitude why pkg` explains why pkg is to be installed.
