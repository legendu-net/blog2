---
title: Fonts for Linux
created: 2013-04-13 00:07:00
date: 2026-04-15 19:27:00.286337
authors:
  - bendu
label: fonts-for-linux
license: CC-BY-4.0
tags:
  - fonts
  - LaTeX
  - Chinese
  - Linux
  - TeX Live
  - TexLive
  - nerd fonts
---

1. `ttf-arphic-uming`, `ttf-wqy-microhei`, `ttf-wqy-zenhei`, `xfonts-wqy` and `ttf-opensymbol`
   are some packages related to Chinese fonts.

1. If you have Adobe Reader installed on your computer,
   you can use Adobe Chinese fonts for free.

1. To check Chinese fonts installed on your computer,
   you can use the command `fc-list :lang=zh-cn | sort`.

1. To install extra fonts in linux,
   you can just copy the font files to the directory '\$HOME/.fonts'.
   To make them in effect,
   you have to run `fc-cache` to update the system fonts cache.

1. If you ever have any fonts problem with Tex Live in Linux,
   install the package `texlive-fonts-extra` (if you haven't done so) and try again.

1. [nerd-fonts](https://github.com/ryanoasis/nerd-fonts)
   patches developer targeted fonts with a high number of glyphs (icons).
   Specifically to add a high number of extra glyphs from popular 'iconic fonts'
   such as Font Awesome, Devicons, Octicons, and others.
