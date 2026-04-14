---
title: Tips on the tar Command in Linux
created: 2023-02-02 13:58:33
date: 2026-04-13 23:14:33.436073
authors:
  - bendu
label: tips-on-the-tar-command-in-linux
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - tar
  - compress
  - decompress
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

--strip-components

--exclude

tar --strip-components=1 -C /usr/local/bin/ -zxvf sccache-v0.4.0-pre.8-x86_64-unknown-linux-musl.tar.gz \*/sccache
