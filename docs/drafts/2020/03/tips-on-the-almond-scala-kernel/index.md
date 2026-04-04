---
title: "Tips on the Almond Scala Kernel"
created: 2020-03-24 18:33:39
date: 2020-03-24 18:33:39
authors:
  - bendu
label: tips-on-the-almond-scala-kernel
license: CC-BY-4.0
tags:
  - Computer Science
  - Scala
  - Almond
  - JupyterLab
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**



1. `kernel.silent(true)` 
    supress outputs of cells.


2. Currently each line in a cell have an output,
    which is messy.
    There are 2 ways to avoid this.

        :::scala
        val resObj = {
            ...
            ...
        }

        {{
            ...
            ...
        }}

## References

[Use Spark with the Almond Scala Kernel in JupyterLab](http://www.legendu.net/misc/blog/spark-almond-jupyterlab/)

[Specify Dependencies in the Almond Scala Kernel in JupyterLab](http://www.legendu.net/misc/blog/scala-almond-dependencies/)