---
title: Yarn for Spark
created: 2021-11-29 12:32:33
date: 2026-04-15 19:27:00.849940
authors:
  - bendu
label: yarn-for-spark
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Spark
  - big data
  - YARN
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. List all Spark applications.

   ```bash
    yarn application --list
   ```

1. Show status of a Spark application.

   ```bash
    yarn application -status application_1459542433815_0002
   ```

1. view logs of a Spark application.

   ```bash
    yarn logs -applicationId application_1459542433815_0002
   ```

1. kill a Spark application.

   ```bash
    yarn application -kill application_1459542433815_0002
   ```
