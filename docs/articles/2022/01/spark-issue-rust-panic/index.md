---
title: 'Spark Issue: Rust Panic'
created: 2022-01-07 11:12:24
date: 2026-04-13 23:14:13.848670
authors:
  - bendu
label: spark-issue-rust-panic
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Spark
  - issue
  - Spark issue
  - big data
  - panic
  - panicked at
  - Rust
---

If you use Rust with Spark/PySpark
and there are issues in the Rust code,
you might get Rust panic error messages.

## Symptom

> Error: b"thread 'main' panicked at 'index out of bounds: the len is 15 but the index is 15', src/game.rs:131:39\\nnote: run with RUST_BACKTRACE=1 environment variable to display a backtrace\\n"

## Cause

Bug in the Rust code.

## Solution

Fix the bug in the Rust code.
