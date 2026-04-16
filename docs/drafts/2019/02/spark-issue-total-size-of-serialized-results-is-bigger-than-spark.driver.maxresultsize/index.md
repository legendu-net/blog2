---
title: 'Spark Issue: Total Size of Serialized Results Is Bigger than spark.driver.maxResultSize'
created: 2019-02-21 12:14:37
date: 2026-04-15 19:27:01.240140
authors:
  - bendu
label: spark-issue-total-size-of-serialized-results-is-bigger-than-spark.driver.maxresultsize
license: CC-BY-4.0
tags:
  - programming
  - Spark
  - issues
  - solutions
  - big data
  - error
  - issue
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Issue

Total size of serialized results is bigger than spark.driver.maxResultSize

## Solutions

1. Eliminate unnecessary `broadcast` or `collect`.

1. If one of the tables for joining contains too large number of partitions
   (which results in too many jobs),
   repartition it to reduce the number of partitions before joining.

1. Make `spark.driver.maxResultSize` larger.

   - set by SparkConf: `conf.set("spark.driver.maxResultSize", "3g")`

   - set by spark-defaults.conf: `spark.driver.maxResultSize 3g`

   - set when calling spark-submit: `--conf spark.driver.maxResultSize=3g`

## References

https://issues.apache.org/jira/browse/SPARK-17556

https://stackoverflow.com/questions/47996396/total-size-of-serialized-results-of-16-tasks-1048-5-mb-is-bigger-than-spark-dr

https://spark.apache.org/docs/latest/configuration.html

https://www.hackingnote.com/en/spark/trouble-shooting/total-size-is-bigger-than-maxResultSize

https://issues.apache.org/jira/browse/SPARK-17556

https://forums.databricks.com/questions/66/how-do-i-work-around-this-error-when-using-rddcoll.html

https://stackoverflow.com/questions/46763214/total-size-of-serialized-results-of-tasks-is-bigger-than-spark-driver-maxresults
