---
title: 'Spark Issue: AnalysisException: Found Duplicated Columns'
created: 2022-04-03 18:51:57
date: 2026-04-15 19:27:00.803773
authors:
  - bendu
label: spark-issue-analysisexception-found-duplicated-columns
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Spark
  - issue
  - error
  - exception
  - AnalysisException
  - duplicated columns
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptoms

> pyspark.sql.utils.AnalysisException: Found duplicate column(s) when inserting into ...

## Possible Causes

As the error message says,
there are duplicated columns in your Spark SQL code.

## Possible Solutions

Fix the duplicated columns issues in your Spark SQL.
For example,
you can remove duplicated columns from your code
or you can use different column names.
