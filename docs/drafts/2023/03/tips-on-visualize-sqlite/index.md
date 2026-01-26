---
title: "Tips on visualize-sqlite"
date: 2023-03-05 21:24:58
modified: 2023-03-05 23:11:15
authors:
  - bendu
label: tips-on-visualize-sqlite
license: CC-BY-4.0
tags:
  - Computer Science
  - programming
  - Rust
  - visualize
  - SQLite3
  - DOT
  - GraphViz
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


[visualize-sqlite](https://github.com/UhhhWaitWhat/visualize-sqlite)
is a Rust crate for creating simple visualizations 
of SQLite databases in GraphViz dot format.

## Installation

    wajig install libsqlite3-dev graphviz
    cargo install visualize-sqlite

## Usage

    visualize-sqlite your_sqlite_database.db | dot -Tpng -Gfontname='Fira Mono' -Gfontcolor='#586e75' -Gbgcolor='#fdf6e3' -Nfontname='Fira Mono' -Nfontcolor='#586e75' -Efontname='Fira Mono' > output.png

