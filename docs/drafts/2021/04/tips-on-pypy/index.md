---
title: Tips on PyPy
created: 2021-04-19 09:53:27
date: 2026-04-13 23:15:04.989844
authors:
  - bendu
label: tips-on-pypy
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - PyPy
  - Python
  - pip
  - ensurepip
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation

1. Download PyPy from https://www.pypy.org/download.html.

1. Unzip it.

1. Install pip.

   :::bash
   /path/to/pypy -m ensurepip
   /path/to/pypy -m pip install ...

### Packages Failed to Install

## pytype

sudo apt install gcc cmake g++

ast27/Parser/tokenizer.c:17:10: fatal error: codecs.h: No such file or directory
