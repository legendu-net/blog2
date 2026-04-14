---
title: Distributions in R
created: 2012-11-05 00:22:23
date: 2026-04-13 23:33:14.646752
authors:
  - bendu
label: distributions-in-r
license: CC-BY-4.0
tags:
  - distribution
  - R
  - programming
  - Statistics
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

4. The definition of geometric distribution in R is not the same as the common definition.
   A random variable of geometric distribution in R starts from zero,
   i.e. geometric distribution in R is defined as the number of failures before we succeed.

1. A random variable of negative binomial distribution $NB(r,p)$ in R
   is defined as the number of failures before we succeed for `r` times,
   where `p` is the success probability in each trial.

1. The definition of hyper-geometric is the same as common but be careful with the parameters!
