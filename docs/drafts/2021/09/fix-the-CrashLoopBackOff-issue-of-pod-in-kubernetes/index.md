---
title: "Fix the CrashLoopBackOff Issue of Pod in Kubernetes"
created: 2021-09-13 22:44:33
date: 2021-09-14 11:30:24
authors:
  - bendu
label: fix-the-CrashLoopBackOff-issue-of-pod-in-kubernetes
license: CC-BY-4.0
tags:
  - Computer Science
  - Software
  - tools
  - k8s
  - Kubernetes
  - pod
  - CrashLoopBackOff
  - container
  - issue
  - error
  - exception
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


Define `command` as `["/busybox/sh", "-c", "tail -f /dev/null"]`
instead of 
`["/busybox/sh", "-c", "tail", "-f", "/dev/null"]`