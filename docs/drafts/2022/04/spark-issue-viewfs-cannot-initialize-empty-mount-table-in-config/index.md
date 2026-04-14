---
title: 'Spark Issue: ViewFs: Cannot Initialize: Empty Mount Table in Config'
created: 2022-04-03 19:17:15
date: 2026-04-13 23:14:49.764221
authors:
  - bendu
label: spark-issue-viewfs-cannot-initialize-empty-mount-table-in-config
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Spark
  - Spark issue
  - ViewFs
  - error
  - exception
  - empty mount table
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptoms

> java.io.IOException: ViewFs: Cannot initialize: Empty Mount table in config for viewfs://cluster-name-ns02/

## Possible Causes

As the error message says,
`viewfs://cluster-name-ns02` is not configured.

1. It is possible that the Spark cluster has just migrated to Router-based Federation (RBF) namenodes,
   but the Spark client is not updated correspondingly.

1. The HDFS path is not configured to be accessible.

## Possible Solutions

1. Ask the Hadoop admin to update the Hadoop/Spark client
   (both the Hadoop binary and configuration files)
   if this is due to lacking of RBF compatibility.

1. Ask the Hadoop admin to configure `viewfs://cluster-name-ns02`
   if the issue is due to misconfiguration.

1. Use a different HDFS path.
