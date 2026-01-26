---
title: "Pointers in C++"
date: 2012-10-21 00:00:00
modified: 2012-10-21 00:00:00
authors:
  - bendu
label: pointers-in-cpp
license: CC-BY-4.0
tags:
  - C++
  - programming
  - pointer
---


## Pointers

0. No pointer, no polymorphism.

1. C/C++ is notorious for raw pointers. 
While pointers can boost up the speed of programs, 
it invites a trillion chances for making mistakes. 
You should avoid using raw pointers, 
instead, 
consider using `unique_ptr`, `shared_ptr` and `weak_ptr`.
They are almost as efficient as raw pointers but much safer to use. 

1. If `p` is a dynamically allocated array, 
you have to use `delete[] p` to delete it when it is no longer required. 

2. `auto_ptr` objects cannot be stored in STL containers, 
because they are not copy-construable or assignable.


