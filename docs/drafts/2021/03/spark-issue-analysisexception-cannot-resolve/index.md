---
title: 'Spark Issue: AnalysisException: Cannot Resolve'
created: 2021-03-24 15:03:48
date: 2026-04-15 19:27:00.934359
authors:
  - bendu
label: spark-issue-analysisexception-cannot-resolve
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Spark
  - issue
  - AnalysisException
  - cannot resolve
  - big data
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom

org.apache.spark.sql.AnalysisException: cannot resolve ...

## Cause

Miss-spell a column name or refer to a column which does not exist in the DataFrame.

## Solution

Correct the column name or add the missing column in the `select` method before using it.
