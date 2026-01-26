---
title: "Logging in PySpark"
date: 2020-06-15 11:38:22
modified: 2020-06-15 11:38:22
authors:
  - bendu
label: logging-in-pyspark
license: CC-BY-4.0
tags:
  - Computer Science
  - big data
  - PySpark
  - Spark
  - loguru
  - logging
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Excessive logging is better than no logging!
    This is generally true in distributed big data applications.
    
2. Use `loguru` if it is available.
    If you have to use the `logging` module,
    be aware of traps in using it.
    For more details, 
    please refer to [Hands on the logging Module in Python](http://www.legendu.net/misc/blog/python-logging-module/).