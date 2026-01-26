---
title: "Profile C++ Code"
date: 2015-06-22 22:01:47
modified: 2015-06-22 22:01:47
authors:
  - bendu
label: profile-c++-code
license: CC-BY-4.0
tags:
  - programming
  - C++
  - profile
  - profiling
  - speed
  - performance
  - Valgrind
  - kcachegrind
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**



You can use valgrind with the following options

```bash
valgrind --tool=callgrind ./(Your binary)
```

It will generate a file called callgrind.out.x. 
You can then use kcachegrind tool to read this file. 
It will give you a graphical analysis of things with results like which lines cost how much.
