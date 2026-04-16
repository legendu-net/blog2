---
title: 'Spark Issue: Unable to Find Encoder Type'
created: 2019-05-21 12:14:37
date: 2026-04-15 19:27:01.203492
authors:
  - bendu
label: spark-issue-unable-to-find-encoder-type
license: CC-BY-4.0
tags:
  - programming
  - Spark
  - issue
  - encoder
  - error
  - big data
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Issue Unable to find encoder for type stored in a Dataset

## Solution

Import Spark implicits in the right scope resolves the issue.

```
import spark.implicits._
```

## References

https://stackoverflow.com/questions/38664972/why-is-unable-to-find-encoder-for-type-stored-in-a-dataset-when-creating-a-dat
