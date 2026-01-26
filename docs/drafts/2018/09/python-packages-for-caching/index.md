---
title: "Serialization and Caching in Python"
date: 2018-09-06 00:59:06
modified: 2021-10-03 23:32:52
authors:
  - bendu
label: python-packages-for-caching
license: CC-BY-4.0
tags:
  - programming
  - Python
  - packages
  - caching
  - lru_cache
  - diskcache
  - memcached
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## functools.lru_cache

https://docs.python.org/3/library/functools.html#functools.lru_cache

## cachetools

https://cachetools.readthedocs.io/en/latest/
https://github.com/tkem/cachetools

## diskcache sounds like a good options!!!

DiskCache: Disk Backed Cache
http://www.grantjenks.com/docs/diskcache/tutorial.html

## memcached & pymemcache

https://pypi.org/project/pymemcache/

http://memcached.org/

Free & open source, high-performance, distributed memory object caching system, generic in nature, 
but intended for use in speeding up dynamic web applications by alleviating database load.

## References 

- [Serialization and deserialization in Python](http://www.legendu.net/misc/blog/serialization-and-deserialization-in-python)

- https://docs.python-guide.org/scenarios/serialization/