---
title: 'Spark Issue: TypeError WithReplacement'
created: 2021-12-17 11:10:13
date: 2026-04-05 19:42:37.717315
authors:
- bendu
label: spark-issue-typeerror-withreplacement
license: CC-BY-4.0
tags:
- Computer Science
- programming
- Spark
- PySpark
- issue
- TypeError
- withReplacement
---
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptoms

> TypeError: withReplacement (optional), fraction (required) and seed (optional) should be a bool, float and number; however, got [<class 'int'>].


## Causes

An integer number (e.g., `1`) is passed to the `fraction` parameter  of the function `DataFrame.sample` in PySpark.

## Solutions

Use a float number (e.g., `1.0`) instead.

