---
title: "Select Columns from Structured Text Files"
created: 2016-06-01 16:15:21
date: 2018-01-01 16:15:21
authors:
  - bendu
label: select-columns-from-structured-text-files
license: CC-BY-4.0
tags:
  - programming
  - Python
  - pandas
  - SQL
  - awk
  - cut
  - text file
  - data manipulation
  - column
  - field
---

## Python pandas

My first choice is pandas in Python. 
However, 
below are some tools for quick and dirty solutions.

## [q](https://github.com/harelba/q) 
```sh
q -t -H 'select c1, c3 from file.txt'
```

## cut
```sh
cut -d\t -f1,3 file.txt
```

## awk
```sh
awk -F'\t' '{print $1 "\t" $3}' file.tsv 
```
Note: neither `cut` nor `awk` honors escaped characters.
For working on complicated structured text files, 
pandas in Python is a much better solution.