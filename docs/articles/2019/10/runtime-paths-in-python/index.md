---
title: "Runtime Paths in Python"
created: 2019-10-18 10:20:43
date: 2019-10-18 10:20:43
authors:
  - bendu
label: runtime-paths-in-python
license: CC-BY-4.0
tags:
  - programming
  - Python
  - runtime paths
---


`__file__` is the path of the Python script.
Note that if you make a sybolic link to a Python script and run the symbolic link, 
then `__file__` is the path of the symbolic link.
Of course, you can use `os.path.realpath` to get real path of files.


`pathlib.Path.cwd()`, `os.getcwd()` and `'.'` returns/represents the path where the Python script was invoked,
which is often different from `__file__`.
