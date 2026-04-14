---
title: OOM in Rust
created: 2023-03-05 13:39:51
date: 2026-04-13 23:14:32.667590
authors:
  - bendu
label: oom-in-rust
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - OOM
  - out of memory
  - SIGKILL
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

SIGKILL (signal 9)

The following error message will be generated if rustc runs out of memory.

signal: 9, SIGKILL: kill

## References

- [Dealing with Out-of-memory Conditions in Rust](https://www.crowdstrike.com/blog/dealing-with-out-of-memory-conditions-in-rust/)

- [逃离编译时的内存溢出](https://rustcc.cn/article?id=00936d90-6190-4e68-8b11-f9da18665267)
