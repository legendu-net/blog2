---
title: Inverse of a Special Class of Matrices with High Dimensions
created: 2010-05-30 22:12:02
date: 2026-04-05 19:42:37.478596
authors:
- bendu
label: inverse-of-a-special-class-of-matrices-with-high-dimensions
license: CC-BY-4.0
tags:
- inverse
- fun problems
- matrix
- math
- statistics
- R
- high dimension
---
<img src="http://www.legendu.net/media/math/matrix-inverse.png"
width="200" height="160" align="right"/>

One day, my officemate Tieming asked me about a problem that she met in her research. 
Suppose $\boldsymbol{B}$ is a symmetric matrix of huge dimension 
and $\boldsymbol{D}$ is a diagonal matrix with nonnegative diagonal elements. 
The inverse of $\boldsymbol{B}$ is already known, 
how can we calculate the inverse of $\boldsymbol{B}+\boldsymbol{D}$ efficiently? 
I thought for a while and found a good way to solve the problem. 
See solution in [Inverse of Matrix](/media/inverse-of-matrix.pdf).

I haven't implemented the algorithm yet, 
but a roughly estimate of the complexity of this algorithm tells me that even R can handle it. 
I will write a R function to do this later when I have time.
