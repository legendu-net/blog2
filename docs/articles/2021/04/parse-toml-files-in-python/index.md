---
title: Parse TOML Files in Python
created: 2021-04-26 09:37:58
date: 2026-04-05 15:40:54.778996
authors:
- bendu
label: parse-toml-files-in-python
license: CC-BY-4.0
tags:
- Computer Science
- programming
- Python
- TOML
- parse
- load
- dump
- tomlkit
---
1. There are 2 popular Python libraries 
    [tomlkit](https://github.com/sdispater/tomlkit)
    and
    [toml](https://github.com/uiri/toml)
    for parsing TOML formatted files in Python.
    [tomlkit](https://github.com/sdispater/tomlkit)
    is preferred to 
    [toml](https://github.com/uiri/toml)
    as it is more flexible and style-preserving.

2. A TOML file always interpret a key (even a bare ASCII integer) as string. 
    For this reason, a dict with numerical keys cannot be serialized using toml.

3. Indentions are allowed in a TOML file.

## References 

- [Hands on the Python Library tomlkit](http://www.legendu.net/misc/blog/hands-on-python-library-tomlkit)

- [Hands on the Python Library toml](http://www.legendu.net/misc/blog/hands-on-python-library-toml)

- [Adopting/recommending a toml parser?](https://discuss.python.org/t/adopting-recommending-a-toml-parser/4068)

