---
title: "RStudio Does Not Start"
date: 2012-05-26 12:45:00
modified: 2015-02-26 12:45:00
authors:
  - bendu
label: rstudio-not-start
license: CC-BY-4.0
tags:
  - IDE
  - R
  - statistics
  - software
  - configuration
  - RStudio
  - CRAN
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

Rstudio is the best cross-platform IDE for R so far. 
It is a lot like the IDE of MATLAB.
Once I came across the problem that Rstudio did not start. 
I search website for a solution but has no luck. 
I have seen broken configuration files prevent applications 
from working correctly a lot.
So I tried removing the configuration directory ".rstudio-desktop" from my home directory, 
and Rstudio worked properly again!
This trick also works for many other applications, 
e.g., forefix, latex (temporary files), etc.

