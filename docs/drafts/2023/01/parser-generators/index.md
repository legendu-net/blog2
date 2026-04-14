---
title: Parser Generators
created: 2023-01-10 11:41:44
date: 2026-04-13 23:14:34.362458
authors:
  - bendu
label: parser-generators
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - parser
  - generator
  - LL(1)
  - LR(1)
  - PEG
  - pest
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [pest](https://crates.io/crates/pest)

[Pest](https://crates.io/crates/pest)
is a general purpose parser written in Rust
with a focus on accessibility, correctness, and performance.
It uses parsing expression grammars (PEG) as input,
which are similar in spirit to regular expressions,
but which offer the enhanced expressivity needed to parse complex languages.

## [peg](https://crates.io/crates/peg)

[peg](https://crates.io/crates/peg)
is a simple Parsing Expression Grammar (PEG) parser generator.

## [lalrpop](https://crates.io/crates/lalrpop)

[lalrpop](https://crates.io/crates/lalrpop)
is a Rust parser generator framework with usability as its primary goal.

## References

- [Learn from LL(1) to PEG parser the hard way](https://ep2021.europython.eu/talks/98ecgon-learn-from-ll1-to-peg-parser-the-hard-way/)
