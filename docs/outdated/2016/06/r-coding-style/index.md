---
title: "R Coding Style"
created: 2016-06-23 16:41:21
date: 2016-10-23 16:41:21
authors:
  - bendu
label: r-coding-style
license: CC-BY-4.0
tags:
  - programming
  - R
  - CRAN
  - formatting
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

1. You can use the function `tidy_souce` in the R package `formatR`
to format R code.
```R
tidy_source('unformatted.r', file = 'formatted.r')
```
However, 
there is a bug in the package `formatR`.
For example, 
the `formatR` fails to work with the following code.
```R
if { # this is comment
    ...
}
```

2. Avoid changing the type of object.

