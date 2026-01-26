---
title: "Copy Object in Python"
date: 2019-10-31 17:22:26
modified: 2019-10-31 17:22:26
authors:
  - bendu
label: copy-object-in-python
license: CC-BY-4.0
tags:
  - programming
  - Python
  - copy object
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

You can use the copy module to copy objects in Python. 
Customized coping behavior can be achived by overriding the methods `__copy__` (for shallow copy)
    and `__deepcopy__` (for deep copy).

## References

https://docs.python.org/3/library/copy.html#copy.deepcopy

https://stackoverflow.com/questions/4794244/how-can-i-create-a-copy-of-an-object-in-python
