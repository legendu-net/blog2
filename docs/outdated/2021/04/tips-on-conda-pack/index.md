---
title: Tips on conda-pack
date: 2021-04-30 12:13:17
modified: 2021-03-30 12:13:17
authors:
- bendu
label: tips-on-conda-pack
license: CC-BY-4.0
tags:
- programming
- conda-pack
- conda
- dependency
- virtual environment

---
**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**
It is suggested that you use python-build-standlone instead of conda-pack to build portable Python environments.
Please refer to
[Packaging Python Dependencies for PySpark Using Python-Build-Standalone](http://www.legendu.net/en/blog/packaging-Python-Dependencies-for-PySpark-Using-python-build-standalone/)
for more details.

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. All packages in a virtual environment must be managed by conda (rather than pip)
    so that it can be packe using conda-pack.

2. When using a conda-pack virtual environment with PySpark,
    the Python package `pyyspark` comes with Spark is automatically injected into PYTHONPATH
    so that users do not have to install `pyspark` into the virtual environemnt by themselves.
    As a matter of fact,
    the `pyspark` comes with Spark is always used
    even if you have a local copy installed 
    when you submit a PySpark application with a conda-pack virtual environment.
    For more discussions,
    please refer to [this isue](https://github.com/conda/conda-pack/issues/102).

## References

[Pack a Conda Virtual Environment](http://www.legendu.net/misc/blog/conda-tips/#pack-a-conda-virtual-environment)

https://conda.github.io/conda-pack/

https://conda.github.io/conda-pack/cli.html

