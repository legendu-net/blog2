---
title: "String in MATLAB"
date: 2012-12-20 10:40:42
modified: 2015-02-20 10:40:42
authors:
  - bendu
label: string-in-MATLAB
license: CC-BY-4.0
tags:
  - string
  - programming
  - MATLAB
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**


1. To display special characters (e.g. `\n`, `\t` and so on),
you have to use `sprintf` to format it first. 
`fprintf` does the job of formatting and printing together.

2. Unlike R, 
numbers in MATLAB will not be silently converted to strings when needed.
You must use the function `num2str` to convert numbers to strings manually.
