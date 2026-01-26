---
title: "Install the Latest Version of Software on Ubuntu"
date: 2022-07-07 22:11:57
modified: 2022-07-07 22:11:57
authors:
  - bendu
label: install-the-latest-version-of-software-on-ubuntu
license: CC-BY-4.0
tags:
  - Computer Science
  - programming
  - Ubuntu
  - PPA
  - snap
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Using PPA

## Using snap

The snap version of a software is usually more up-to-date
than the version installed using `apt-get`.
For example,
NevoVim (installed using `apt-get`) on Ubuntu 20.04 is 0.4.1 which is seriously outdated.
You can install the latest version of NeoVim using the following command.

    :::bash
    sudo snap install nvim --classic

