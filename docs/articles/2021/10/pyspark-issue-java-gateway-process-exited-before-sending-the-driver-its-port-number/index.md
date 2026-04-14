---
title: 'PySpark Issue: Java Gateway Process Exited Before Sending the Driver Its Port Number'
created: 2021-10-10 14:23:22
date: 2026-04-13 23:14:10.495270
authors:
  - bendu
label: pyspark-issue-java-gateway-process-exited-before-sending-the-driver-its-port-number
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - PySpark
  - Spark
  - Java
  - Python
  - big data
  - JAVA_HOME
---

I countered the issue when using PySpark locally
(the issue can happen to a cluster as well).
It turned out to be caused by a misconfiguration of the environment variable `JAVA_HOME` in Docker.

## References

[PySpark: Exception: Java gateway process exited before sending the driver its port number](https://stackoverflow.com/questions/31841509/pyspark-exception-java-gateway-process-exited-before-sending-the-driver-its-po)
