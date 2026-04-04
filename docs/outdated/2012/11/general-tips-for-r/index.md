---
title: "General Tips for R"
created: 2012-11-05 00:29:52
date: 2013-12-05 00:29:52
authors:
  - bendu
label: general-tips-for-r
license: CC-BY-4.0
tags:
  - tips
  - R
  - generic
  - programming
  - argument
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**


1. Many R functions have lots of arguments which allows you get a full
control of their behaviors, so before you ask whether there is any R
function which have a little different behavior from a R function
you know, you'd better first check the arguments of the function you
know.

2. Many R functions are generic functions (e.g. `plot`, `residuals`, `coef`, etc), 
which means that they can be
applied to different types of objects, and the behavior varies
according to the type of objects.
