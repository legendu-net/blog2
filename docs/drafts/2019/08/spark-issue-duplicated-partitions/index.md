---
title: 'Spark Issue: Duplicated Partitions'
created: 2019-08-21 12:14:37
date: 2026-04-15 19:27:01.165751
authors:
  - bendu
label: spark-issue-duplicated-partitions
license: CC-BY-4.0
tags:
  - programming
  - Spark
  - issue
  - duplicate
  - overwrite
  - big data
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

There seems to be an issue in Spark that it might fail to overwrite files
even if mode of `spark.write` is set to be "overwrite".
