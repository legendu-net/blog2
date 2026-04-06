---
title: Initializing Variables in C++
created: 2012-10-19 13:45:33
date: 2026-04-05 19:42:37.277999
authors:
- bendu
label: initializing-variables-in-c++
license: CC-BY-4.0
tags:
- initialization
- C++
- programming
---
1. `{}` is more powerful than `()` and thus is preferred over `()`. 
You should use always use `{}` except for a few cases where `()` is necessary.
For example, 
if you want to create a vector of length 1000, 
you have to use 

        vector<int>(1000);

instead of 

        vector<int> {1000};

which create a vector with one element 1000.

2. Objects in C++ are intialized to have some value when they are created,
i.e., an object in C++ always have a valid value. 
This is different from Java. 
In Java, objects are essentially references. 
If an object in Java does not point to any memory when initializing, 
it is `null`. 
In C++, 
it is impossible to have `null` object. 
You can only have `null` pointers in C++.

3. Universal initialization list `{}` is very powerful and convenient,
especially when working with containers. 
However you cannot initialize non-const reference using `{}`
using g++ 4.7, 
which seems to be a bug. 
