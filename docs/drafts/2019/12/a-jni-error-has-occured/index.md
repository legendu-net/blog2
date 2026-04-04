---
title: "A JNI Error Has Occured"
created: 2019-12-03 10:14:14
date: 2019-12-03 10:14:14
authors:
  - bendu
label: a-jni-error-has-occured
license: CC-BY-4.0
tags:
  - programming
  - Java
  - JNI error
  - dependency management
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Error Messages

Error: A JNI error has occurred, please check your installation and try again 

Caused by: java.lang.ClassNotFoundException: org.apache.spark.sql.SparkSession


## Cause

Some dependencies (Spark in this case) is not specified as a runtime dependency.
It is often a good idea to exlucde Spark from the runtime dependencies
and only specify it as test dependencies.
However, 
you will not be able to run your code directly in local.
Test can still be run of course.
