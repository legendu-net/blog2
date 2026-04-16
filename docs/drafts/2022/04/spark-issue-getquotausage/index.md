---
title: 'Spark Issue: GetQuotaUsage'
created: 2022-04-03 18:42:10
date: 2026-04-15 19:27:00.815285
authors:
  - bendu
label: spark-issue-getquotausage
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Spark
  - issue
  - exception
  - error
  - getQuotaUsage
  - getContentSummary
  - quota
  - Router
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom I

> py4j.protocol.Py4JJavaError: An error occurred while calling o156.getQuotaUsage.

## Symptom II

> org.apache.hadoop.ipc.RemoteException(java.io.IOException): The quota system is disabled in Router.

## Possible Causes

As the error message in symptom II,
the quota system is disabled in Router.

## Possible Solutions

Remove the usage of `org.apache.hadoop.fs.FileSystem.getQuotaUsage` from the code.
You can use other alternatives,
e.g.,
you can use `org.apache.hadoop.fs.FileSystem.getContentSummary(path_hdfs).getLength()`
if you just need the size of a HDFS path.
