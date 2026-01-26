---
title: "Change the Default Shell in Linux"
date: 2025-12-07 17:48:30
modified: 2025-12-22 20:04:26
authors:
  - bendu
label: change-the-default-shell-in-linux
license: CC-BY-4.0
tags:
  - Computer Science
  - programming
  - Linux
  - shell
  - chsh
  - Atomic
  - change
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Atomic Linux Distributions

[How to change the default shell in fedora silverblue?](https://discussion.fedoraproject.org/t/how-to-change-the-default-shell-in-fedora-silverblue/21203/10)

```
sudo usermod --shell $(which fish) $(id -un)
```

## Mutable Linux Distributions

```
sudo chsh -s $(which fish) $(id -un)
```
You have to add the path of `fish` into `/etc/shells`,
if you get the error message
"chsh: /usr/bin/fish is an invalid shell".

Log out and then log in (or simplify reboot) for the change to take effect.
