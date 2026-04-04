---
title: Ruff Is An Extremely Fast Python Linter Written in Rust
date: 2023-04-01 18:21:35
modified: 2026-04-03 22:47:00.461511
authors:
- bendu
label: ruff-is-an-extremely-fast-python-linter-written-in-rust
license: CC-BY-4.0
tags:
- Computer Science
- programming
- Python
- Ruff
- lint
- linter
- formatting
---
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Use ruff In a uv Managed Python Project

    uv run ruff check 
    uv run ruff format . 

## Use ruff Standalone 

The most convenient way to use run ruff standalone is via `uvx`.

    uvx ruff check /some/path
    uvx ruff format /some/path
    
## Format Python Scripts with Indention Width = 2

    ruff format --config indent-width=2 path/to/file.py

## Formatting Code in Jupyter Notebooks and Markdown Files

1. Ruff supports formatting Python code in Jupyter notebooks.

2. As of early 2026,
    Ruff supports formatting code blocks in Markdown files 
    as a preview feature.

## References

- [ruff @ GitHub](https://github.com/astral-sh/ruff)

- [ruff config - pylint](https://github.com/pylint-dev/pylint/blob/47cb11f4cb01a61f83d915d88e828f103a479980/pyproject.toml)
