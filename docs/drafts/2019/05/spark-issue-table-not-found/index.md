---
title: 'Spark Issue: Table Not Found'
created: 2019-05-24 15:06:53
date: 2026-04-15 19:27:01.183930
authors:
  - bendu
label: spark-issue-table-not-found
license: CC-BY-4.0
tags:
  - programming
  - Spark
  - issue
  - big data
  - error
  - hive-site.xml
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom 1

org.apache.spark.sql.AnalysisException: Table not found

## Symptom 2

java.lang.RuntimeException: Table Not Found: my_rdd

## Cause 1

Miss-spelled a table name.

## Solution 1

Correct miss-spelling.

## Cause 2

Forgot to submit a `hive-site.xml` together with the Spark application.

## Solution 2

Include Hive configuration of the Spark cluster when submitting Spark jobs.

```
:::bash
--files "/apache/spark/conf/hive-site.xml"
```
