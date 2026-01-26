---
title: "Combination and Permutation Related Functions in R"
date: 2010-11-20 00:00:00
modified: 2010-11-20 00:00:00
authors:
  - bendu
label: combination-and-permutation-in-r
license: CC-BY-4.0
tags:
  - R
  - statisitcs
  - combination
  - permutation
  - programming
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**



1. `expand.grid` creates a data frame from all possible combinations of supplied vectors or factors. 
For example,

        > expand.grid(letters[1:2], 1:3, c("+", "-"))
           Var1 Var2 Var3
        1     a    1    +
        2     b    1    +
        3     a    2    +
        4     b    2    +
        5     a    3    +
        6     b    3    +
        7     a    1    -
        8     b    1    -
        9     a    2    -
        10    b    2    -
        11    a    3    -
        12    b    3    -
            

2. `combn` generates all combinations of $n$ elements taking $m$ at a time.
