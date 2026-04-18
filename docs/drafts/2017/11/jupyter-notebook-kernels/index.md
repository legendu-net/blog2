---
title: Jupyter Notebook Kernels
created: 2017-11-11 10:39:11
date: 2026-04-17 18:08:09.095319
authors:
  - bendu
label: jupyter-notebook-kernels
license: CC-BY-4.0
tags:
  - software
  - Jupyter
  - notebook
  - JupyterLab
  - kernel
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

[Jupyter Kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)

By default,
Python kernels are installed to `/usr/local/share/jupyter/kernels`
and BeakerX kernels are installed to `/usr/share/jupyter/kernels`.

## Python

### [ipykernel](https://github.com/ipython/ipykernel)

IPython Kernel for Jupyter/Lab,
which is the default Python kernel for Jupyter/Lab currently.

### [xeus-python](https://github.com/jupyter-xeus/xeus-python)

`xeus-python` is a Jupyter kernel for Python
based on the native implementation of the Jupyter protocol [xeus](https://github.com/jupyter-xeus/xeus).

[A new Python kernel for Jupyter](https://blog.jupyter.org/a-new-python-kernel-for-jupyter-fcdf211e30a8)

## SQL Kernels

There are multiple ways to run SQL in a Jupyter notebook.

- using a dedicated SQL kernel
- using cell magics
- using a Python library (in a notebook with a Python kernel)

I personally prefer running SQL through a Python library.

- No need to install dedicated SQL kernels or kernels support cells magics for SQL.
- We often need to do data transformation and visualization after querying data.
  This is convenient to do in Python.

## Spark Kernel

There are dedicated kernels for Spark, e.g.,

1. toree (a good one）
1. sparkmagic (seems like a good choice)
1. spylon-kernel

However,
such a Spark kernel isn't really needed
no matter you use
[Spark/Scala](use-spark-with-the-almond-scala-kernel-in-jupyterlab)
or
[PySpark](process-big-data-using-pyspark) (preferred)
.

## JVM Language Kernels

- [JJava](https://github.com/dflib/jjava)

- [rapaio-jupyter-kernel](https://github.com/padreati/rapaio-jupyter-kernel)

- [Ganymede](https://github.com/allen-ball/ganymede)

  - works well for Java
  - print doesn't work for other JVM languages based on cell magics

- [kotlin-jupyter](https://github.com/Kotlin/kotlin-jupyter)

  - Kotlin 2 is not supported yet

- [almond](https://github.com/almond-sh/almond)

  - works well

## Remote Kernels

IPython is able to run remtoe kernels.

https://github.com/ipython/ipython/wiki/Cookbook:-Connecting-to-a-remote-kernel-via-ssh

https://stackoverflow.com/questions/29037211/how-do-i-add-a-kernel-on-a-remote-machine-in-ipython-jupyter-notebook

https://github.com/jupyter/notebook/issues/1487
