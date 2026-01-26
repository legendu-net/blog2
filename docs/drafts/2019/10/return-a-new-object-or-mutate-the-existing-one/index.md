---
title: "Return a New Object Or Mutate the Existing Object"
date: 2019-10-31 17:09:56
modified: 2019-10-31 17:09:56
authors:
  - bendu
label: return-a-new-object-or-mutate-the-existing-one
license: CC-BY-4.0
tags:
  - programming
  - Python
  - design pattern
  - copy
  - mutate
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Generally speaking,
prefer to return a new object rather than mutating the existing object.
This is true in most programming languages besides C who seeks for best peformance.


The pandas package in Python keeps a good balance between good design and performance.
By default, 
pandas always return a copy.
When a DataFrame is large (and performance matteers),
in-place changes on the DataFrame (rather than copy) can be made by specifying the option `inplace=True`.


## References

[Idiomatic Python - return new object or mutate the existing one?](https://www.reddit.com/r/learnpython/comments/2931ph/idiomatic_python_return_new_object_or_mutate_the/)
