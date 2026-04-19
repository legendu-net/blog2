---
title: Get CentOS Version
created: 2022-01-01 13:47:32
date: 2026-04-13 23:14:13.406075
authors:
  - bendu
label: get-centos-version
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - CentOS
  - Linux
  - version
  - Spark
  - big data
---

You can get the version of CentOS
using the following command.

```bash
rpm -q centos-release
```

This trick can be used to get the version of the CentOS distribution on a Spark cluster.
Basically,
you run this command in the driver or workers to print the versions
and then parse the log of the Spark application.

```python
#!/usr/bin/env python3
import subprocess as sp
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CentOS_Version") \
    .enableHiveSupport().getOrCreate()
sp.run("rpm -q centos-release", shell=True, check=True)
```
