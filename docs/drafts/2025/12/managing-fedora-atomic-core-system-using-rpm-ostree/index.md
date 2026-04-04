---
title: "Managing Fedora Atomic Core System Using rpm-ostree"
created: 2025-12-07 18:19:15
date: 2025-12-07 20:40:15
authors:
  - bendu
label: managing-fedora-atomic-core-system-using-rpm-ostree
license: CC-BY-4.0
tags:
  - Computer Science
  - programming
  - Linux
  - atomic
  - Fedora
  - rpm
  - ostree
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


Fedora Atomic Linux ditributions use 
`rpm-ostree` to install system tools.

## Upgrade

```
sudo ostree admin pin 0
rpm-ostree rebase
rpm-ostree rebase fedora:fedora/43/x86_64/kinoite
```


