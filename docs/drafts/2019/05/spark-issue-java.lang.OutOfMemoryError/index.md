---
title: "Spark Issue: java.lang.OutOfMemoryError"
date: 2019-05-26 10:19:41
modified: 2021-03-26 10:19:41
authors:
  - bendu
label: spark-issue-java.lang.OutOfMemoryError
license: CC-BY-4.0
tags:
  - programming
  - Spark
  - issue
  - big data
  - OutOfMemoryError
  - OOM
  - error
  - Spark issue
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom

OutOfMemoryError

## Cause

`java.lang.OutOfMemoryError` is thrown when there is not enough heap memory (for JVM to allocating new objects).

## Solution

Increase executor memory.

    :::bash
    --executor-memory=20G

## Reference:

http://stackoverflow.com/questions/27462061/why-does-spark-fail-with-java-lang-outofmemoryerror-gc-overhead-limit-exceeded
