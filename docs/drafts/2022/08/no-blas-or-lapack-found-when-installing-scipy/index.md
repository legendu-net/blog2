---
title: No BLAS or LAPACK Found When Installing Scipy
created: 2022-08-02 01:15:16
date: 2026-04-13 23:14:43.598977
authors:
  - bendu
label: no-blas-or-lapack-found-when-installing-scipy
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Python
  - scipy
  - BLAS
  - LAPACK
  - issue
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

> To build Scipy from sources, BLAS & LAPACK libraries need to be installed.
> See site.cfg.example in the Scipy source directory and

```
:::bash
sudo apt-get install gfortran libopenblas-dev liblapack-dev
```

The dependency requires scipy 1.6.1 which does not have a pre-built wheel,
thus a wheel will be built when installing scipy 1.6.1
which requires BLAS and LAPACK libraries to be installed.
