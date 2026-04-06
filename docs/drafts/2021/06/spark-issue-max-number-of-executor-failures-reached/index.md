---
title: 'Spark Issue: Max Number of Executor Failures Reached'
created: 2021-06-09 14:44:30
date: 2026-04-05 19:42:37.734683
authors:
- bendu
label: spark-issue-max-number-of-executor-failures-reached
license: CC-BY-4.0
tags:
- Computer Science
- programming
- Spark
- big data
- Spark issue
- executor
- failures
---
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom

21/06/01 15:03:28 INFO ApplicationMaster: Final app status: FAILED, exitCode: 11, (reason: Max number of executor failures (6) reached)

## Possible Causes

The option `spark.yarn.max.executor.failures`
is set to a value which is too small.
In my case,
I believe the Hadoop team misconfigured the option when they update the version of Spark.

## Possible Solutions

By default,
`spark.yarn.max.executor.failures`
is set to $numExecutors \times 2$.
A simple fix is to manually set 
`spark.yarn.max.executor.failures`
to $numExecutors \times 2$.
