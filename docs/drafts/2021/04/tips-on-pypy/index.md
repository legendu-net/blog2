---
title: "Tips on PyPy"
created: 2021-04-19 09:53:27
date: 2021-04-19 09:53:27
authors:
  - bendu
label: tips-on-pypy
license: CC-BY-4.0
tags:
  - Computer Science
  - programming
  - PyPy
  - Python
  - pip
  - ensurepip
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation

1. Download PyPy from https://www.pypy.org/download.html.

2. Unzip it.

3. Install pip.

    :::bash
    /path/to/pypy -m ensurepip
    /path/to/pypy -m pip install ...

### Packages Failed to Install 
## pytype

wajig install gcc cmake g++

ast27/Parser/tokenizer.c:17:10: fatal error: codecs.h: No such file or directory