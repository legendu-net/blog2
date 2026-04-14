---
title: 'Spark Issue: InvalidResourceRequestException'
created: 2021-12-09 10:03:44
date: 2026-04-13 23:14:52.576555
authors:
  - bendu
label: spark-issue-invalidresourcerequestexception
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Spark
  - spark issue
  - issue
  - InvalidResourceRequestException
  - virtual cores
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptoms

Final app status: FAILED, exitCode: 10, (reason: Uncaught exception: org.apache.hadoop.yarn.exceptions.InvalidResourceRequestException: Invalid resource request, requested virtual cores < 0, or requested virtual cores > max configured, requestedVirtualCores=16, maxVirtualCores=8

## Causes

Each Spark node have at most 8 cores and the max possible number for `--executor-cores` is 8
while the configuration requested `--executor-cores` to be 16.

## Solutions

Set `--executor-cores` to be 8.

```
:::bash
--executor-cores 8
```
