---
title: 'Spark Issue: Too Many Containers Asked'
created: 2019-05-21 12:14:37
date: 2026-04-15 19:27:01.187888
authors:
  - bendu
label: spark-issue-too-many-containers-asked
license: CC-BY-4.0
tags:
  - programming
  - Spark
  - issue
  - big data
  - dynamic allocation
  - error
  - container
  - resource
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Error Message

> org.apache.hadoop.yarn.exceptions.InvalidResourceRequestException: Too many containers asked, 16731530.

![image](https://user-images.githubusercontent.com/824507/57563512-99b88f80-7353-11e9-8993-aee9a302c209.png)

## Possible Causes

"Too many containers asked" is a protection mechanism of the Resource Manager.
It might be triggered when dynamic allocation is enabled.

## Solutions

Generally speaking,
it is a good idea to turn on dynamic allocation.
However,
there is some issues in yarn/Spark which can cause the Spark cluster to allocate too many containers.
One simple fix for this issue is to restrict the maximum number of executors.

```
    ...
    --conf spark.dynamicAllocation.enabled=true \
    --conf spark.dynamicAllocation.maxExecutors=1000 \
    ...
```
