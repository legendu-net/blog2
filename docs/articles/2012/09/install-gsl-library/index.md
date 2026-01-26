---
title: "Install the GSL Library"
date: 2012-09-19 13:41:31
modified: 2015-02-19 13:41:31
authors:
  - bendu
label: install-gsl-library
license: CC-BY-4.0
tags:
  - Debian
  - C/C++
  - Linux
  - programming
  - GSL
---

GSL is an advance C/C++ library that is widely used. 
To install GSL, 
you can download the source file and 
following instruction in the included README and INSTALL document. 
For Unix/Linux users, 
the GSL library is often availabe in the repository. 
For example, you can use the following command to install the GSL library in Debian.

    wajig install libgsl0-dev

This will install the GSL library to the default location, 
so that you do not have specify the `-I` and `-L` options for the GSL library. 
However, 
you still have to use the option `-lgsl` and `-lgslcblas` 
(can be replaced by other available BLAS libraries) in order to compile your code using GSL.
