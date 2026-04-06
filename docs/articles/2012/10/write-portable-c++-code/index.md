---
title: Write Portable C++ Code
created: 2012-10-21 00:00:00
date: 2026-04-05 19:42:37.293421
authors:
- bendu
label: write-portable-c++-code
license: CC-BY-4.0
tags:
- C++
- programming
- portable
---
1. Addresses on 64 and 32 OS are different, 
so you have to be careful when your program have to deal with address. 
For example, 
if you take the difference of two pointers/iterators, 
you should type `std::ptrdiff_t` (which is essentially a singed integer type). 
Using an arbitrary integer type makes you code non-portable. 

2. `std::size_t` represents the unsigned native integer size 
on the current architecture (i.e. 16-bit, 32-bit or 64-bit) compiling the code. 
So, to make your code portable,
you should decare indexing variables in loops as `std::size_t` instead of `int` or `unsigned int`.
