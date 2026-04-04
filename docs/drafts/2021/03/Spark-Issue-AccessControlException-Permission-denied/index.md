---
title: "Spark Issue: AccessControlException: Permission Denied"
created: 2021-03-24 14:59:52
date: 2021-03-24 14:59:52
authors:
  - bendu
label: Spark-Issue-AccessControlException-Permission-denied
license: CC-BY-4.0
tags:
  - Computer Science
  - programming
  - Spark
  - issue
  - big data
  - Spark issue
  - AccessControlException
  - permission
  - denied
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


## Symptom

org.apache.hadoop.security.AccessControlException: Permission denied ...

## Cause
The user of the Spark application has no permission to the query a table or HDFS path.

## Solution

Apply to access to the table to query.