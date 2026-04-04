---
title: "Relative Import in Python"
created: 2020-04-12 10:08:43
date: 2020-04-12 10:08:43
authors:
  - bendu
label: relative-import-in-python
license: CC-BY-4.0
tags:
  - Computer Science
  - Python
  - class
---

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


1. Call the package outside it

2. Add `..` into `sys.path`.

    :::python
    import sys
    sys.path.append("..")


## References

[beyond top level package error in relative import](https://stackoverflow.com/questions/30669474/beyond-top-level-package-error-in-relative-import)

[How to do relative imports in Python?](https://stackoverflow.com/questions/72852/how-to-do-relative-imports-in-python)