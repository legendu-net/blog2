---
title: Check the CPU Limit of a Docker Container
created: 2020-12-19 12:18:45
date: 2026-04-13 23:15:08.499124
authors:
  - bendu
label: check-the-cpu-limit-of-a-docker-container
license: CC-BY-4.0
tags:
  - computer science
  - Docker
  - container
  - CPU
  - limit
  - cpuacct
  - cgroup
  - cfs_quota_us
  - cfs_period_us
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Get the number in the file `/sys/fs/cgroup/cpu,cpuacct/cpu.cfs_quota_us`.
   Denote it as `cfs_quota_us`.

1. Get the number in the file `/sys/fs/cgroup/cpu,cpuacct/cpu.cfs_period_us`.
   Denote it as `cfs_period_us`.

1. Calculate the CPU limit (set by `--cpus`) as `cfs_quota_us / cfs_period_us`.
