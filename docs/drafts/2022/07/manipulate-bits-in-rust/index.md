---
title: Manipulate Bits in Rust
created: 2022-07-18 16:54:20
date: 2026-04-13 23:14:44.491549
authors:
  - bendu
label: manipulate-bits-in-rust
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - bit
  - manipulate
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [bitvec](https://crates.io/crates/bitvec)

[bitvec](https://crates.io/crates/bitvec)
Addresses memory by bits, for packed collections and bitfields
bitvec provides a foundational API for bitfields in Rust. It specializes standard-library data structures (slices, arrays, and vectors of bool) to use one-bit-per-bool storage, similar to std::bitset<N> and std::vector<bool> in C++.

## [bit-iter](https://crates.io/crates/bit-iter)

[bit-iter](https://crates.io/crates/bit-iter)
Iterate forward or backwards over the positions of set bits in a word.

## [bit-vec](https://crates.io/crates/bit-vec)

[bit-vec](https://crates.io/crates/bit-vec)
A vector of bits

## [bit_field](https://crates.io/crates/bit_field)

[bit_field](https://crates.io/crates/bit_field)
Simple bit field trait providing get_bit, get_bits, set_bit, and set_bits methods for Rust's integral types.

## [bitfield](https://crates.io/crates/bitfield)

[bitfield](https://crates.io/crates/bitfield)
provides macros to generate bitfield-like struct.

## [bilge](https://crates.io/crates/bilge)

[Bilge](https://crates.io/crates/bilge)
allows you to use bitsized types as if they were a feature of rust.
