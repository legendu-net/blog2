---
title: 'Spark Issue: RuntimeException: Could not find any configured addresses for URI'
created: 2022-03-27 17:24:15
date: 2026-04-13 23:14:50.052349
authors:
  - bendu
label: spark-issue-runtimeexception-could-not-find-any-configured-addresses-for-uri
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Spark
  - Spark issue
  - RuntimeException
  - URI
  - address
  - RBF
  - router-based federation
  - namenode
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptoms

> Caused by: java.lang.RuntimeException: Could not find any configured addresses for URI hdfs://clustername-router/

## Possible Causes

This is due to missing `clustername-router` settings in the property `dfs.nameservices` in `hdfs-site.xml`.
It happens when HDFS migrates to router-based federation (RBF)
but the Hadoop client (which is used to submit the Spark application)
is not updated accordingly.

## Possible Solutions

Ask Hadoop admin to fix the configuration issues.
