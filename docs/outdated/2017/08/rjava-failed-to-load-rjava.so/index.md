---
title: "rJava Failed to Load rJava.So"
date: 2017-08-06 08:01:26
modified: 2017-09-06 08:01:26
authors:
  - bendu
label: rjava-failed-to-load-rjava.so
license: CC-BY-4.0
tags:
  - programming
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

rJava failed to load rJava.so and libjvm.so

Reconfigure Java for R using the command below resolves the issue.

    sudo R CMD javareconf
