---
title: "Spark Issue: UriSyntaxException"
date: 2022-03-27 17:16:54
modified: 2022-03-27 17:16:54
authors:
  - bendu
label: spark-issue:-URISyntaxException
license: CC-BY-4.0
tags:
  - Computer Science
  - programming
  - Spark
  - big data
  - spark issue
  - issue
  - URISyntaxException
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptoms

> java.lang.IllegalArgumentException: java.net.URISyntaxException: Relative path in absolute URI: hdfs::/cluster-name/user/dclong/feature_example/features/train/2022-03-11

## Possible Causes

As the error message points out,
there's a syntax error in the HDFS path.

## Possible Solutions

Correcting `hdfs::/cluster-name/user/dclong/feature_example/features/train/2022-03-11`
to
`hdfs:/cluster-name/user/dclong/feature_example/features/train/2022-03-11`
fixes the issue
.
