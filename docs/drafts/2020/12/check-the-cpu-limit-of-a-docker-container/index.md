---
title: "Check the CPU Limit of a Docker Container"
date: 2020-12-19 12:18:45
modified: 2020-12-19 12:18:45
authors:
  - bendu
label: check-the-cpu-limit-of-a-docker-container
license: CC-BY-4.0
tags:
  - Computer Science
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

2. Get the number in the file `/sys/fs/cgroup/cpu,cpuacct/cpu.cfs_period_us`.
    Denote it as `cfs_period_us`.

3. Calculate the CPU limit (set by `--cpus`) as `cfs_quota_us / cfs_period_us`.