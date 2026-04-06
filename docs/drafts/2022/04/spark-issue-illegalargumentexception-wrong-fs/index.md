---
title: 'Spark Issue: IllegalArgumentException: Wrong FS'
created: 2022-04-03 19:36:50
date: 2026-04-05 19:42:37.687035
authors:
- bendu
label: spark-issue-illegalargumentexception-wrong-fs
license: CC-BY-4.0
tags:
- Computer Science
- programming
- Spark
- Spark issue
- error
- exception
- IllegalArgumentException
- FS
- ViewFs
---
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptoms

> java.lang.IllegalArgumentException: Wrong FS: hdfs://..., expected: viewfs://...

## Possible Causes

The Spark cluster has migrated to Router-based Federation (RBF) namenodes,
and `viewfs://` (instead of `hdfs://`) is required to access HDFS paths.  

## Possible Solutions

1. Use `viewfs://` instead of `hdfs://`.

2. Use relative HDFS paths (without `viewfs://` or `hdfs://` prefixes).

