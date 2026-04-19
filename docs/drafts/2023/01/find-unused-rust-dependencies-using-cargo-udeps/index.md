---
title: Find Unused Rust Dependencies Using cargo-udeps
created: 2023-01-18 20:47:16
date: 2026-04-15 19:27:00.726785
authors:
  - bendu
label: find-unused-rust-dependencies-using-cargo-udeps
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - Cargo
  - deps
  - dependency
  - udeps
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

[cargo-udeps](https://github.com/est31/cargo-udeps)
helps find unused dependencies in Cargo.toml.

## Installation

```bash
cargo install cargo-udeps
```

## Usage

```bash
cargo +nightly udeps
```

## References

- [cargo-udeps @ GitHub](https://github.com/est31/cargo-udeps)

- [Deps.rs - Keep your dependencies up-to-date](https://deps.rs/)
