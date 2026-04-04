---
title: "ImportError: Attempted Relative Import With No Known Parent Package"
created: 2021-09-03 22:42:09
date: 2021-09-03 22:48:45
authors:
  - bendu
label: python-importerror-attempted-relative-import-with-no-known-parent-package
license: CC-BY-4.0
tags:
  - Computer Science
  - programming
  - Python
  - ImportError
  - module
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Symptom

ImportError: Attempted Relative Import With No Known Parent Package

## Solution

The best solution is to run the Python script as a Python module.
However,
you have to add the directory containing the Python module into the Python module search path first.
A simple way to do this is to define the `PYTHONPATH` environemnt variable.

    :::bash
    PYTHONPATH=/root/xinstall/ python3 -m xinstall.main -h

## References

[ImportError: Attempted Relative Import With No Known Parent Package (Python)](https://techwithtech.com/importerror-attempted-relative-import-with-no-known-parent-package/)
