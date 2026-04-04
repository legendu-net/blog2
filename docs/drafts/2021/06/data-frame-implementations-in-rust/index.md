---
title: "Data Frame Implementations in Rust"
created: 2021-06-09 22:38:27
date: 2023-01-07 12:45:14
authors:
  - bendu
label: data-frame-implementations-in-rust
license: CC-BY-4.0
tags:
  - Computer Science
  - programming
  - Rust
  - DataFrame
  - data frame
---
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [Polars](https://github.com/pola-rs/polars)
[Polars](https://github.com/pola-rs/polars)
is a fast multi-threaded DataFrame library in Rust and Python.

## [datafusion](https://github.com/apache/arrow-datafusion)
[datafusion](https://github.com/apache/arrow-datafusion)
is an extensible query execution framework, written in Rust, 
that uses Apache Arrow as its in-memory format.
DataFusion supports both an SQL and a DataFrame API 
for building logical query plans as well as a query optimizer 
and execution engine capable of parallel execution 
against partitioned data sources (CSV and Parquet) using threads.
DataFusion also supports distributed query execution via the Ballista crate.

[Ballista](https://github.com/apache/arrow-datafusion/tree/master/ballista)
is a distributed compute platform primarily implemented in Rust, and powered by Apache Arrow. 
It is built on an architecture that allows other programming languages (such as Python, C++, and Java) 
to be supported as first-class citizens without paying a penalty for serialization costs.


