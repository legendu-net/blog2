---
title: "Sum Type in Rust"
date: 2022-01-15 14:09:38
modified: 2022-01-15 14:09:38
authors:
  - bendu
label: sum-type-in-rust
license: CC-BY-4.0
tags:
  - Computer Science
  - programming
  - Rust
  - sum
  - type
  - Enum
  - either
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


Enum is the preferred way to constrcut a sum type of several types 
(which does not implemente the same trait).

The Rust crate
[either](https://crates.io/crates/either)
provides an enum `Either` (with variants `Left` and `Right`)
which is a general purpose sum type with two cases.
