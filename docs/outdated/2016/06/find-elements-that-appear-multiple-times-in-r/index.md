---
title: Find Elements That Appear Multiple Times in R
created: 2016-06-11 15:31:16
date: 2026-04-05 19:42:39.185545
authors:
- bendu
label: find-elements-that-appear-multiple-times-in-r
license: CC-BY-4.0
tags:
- programming
- CRAN
- R
- frequency
- table
- multiple times
- unique
---
**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

```R
freq = tapply(x, x, FUN=length, simplify=TRUE)
freq[freq > 1]
# or you can use
freq = table(x, useNA = "always")
freq[freq > 1]
```
