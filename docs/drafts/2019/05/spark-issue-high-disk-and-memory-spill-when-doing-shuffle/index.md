---
title: "Spark Issue: High Disk and Memory Spill When Doing Shuffle"
created: 2019-05-24 15:08:21
date: 2021-03-24 15:08:21
authors:
  - bendu
label: spark-issue-high-disk-and-memory-spill-when-doing-shuffle
license: CC-BY-4.0
tags:
  - programming
  - Spark
  - issue
  - big data
  - error
  - memory
  - disk
  - spill
  - Spark issue
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symtom

High disk and memory spill when doing shuffle.

## Cause

Insufficient executor memory (you can monitor this spill metrics from Spark UI).

## Solution

1. Increase executor memory. 

        ::bash
        --executor-memory=4G

2. For jobs that do not need to persist data in memory 
    we can reduce the cache storage size and enlarge the memory portion for shuffle.

        :::bash
        --conf spark.shuffle.memoryFraction=0.4 
        --conf spark.storage.memoryFraction=0.1 
