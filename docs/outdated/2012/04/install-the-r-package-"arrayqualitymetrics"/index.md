---
title: Install the R Package "arrayQualityMetrics"
created: 2012-04-11 19:11:28
date: 2026-04-05 19:42:39.404347
authors:
- bendu
label: install-the-r-package-"arrayqualitymetrics"
license: CC-BY-4.0
tags:
- research
- programming
- biostatistics
- package
- arrayQualityMetrics
- R
- CRAN
---
**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**


I had to use the R package "arrayQualityMetrics" to check the quality of some gene chips. 
Installing this package in Linux takes a few steps. 
The following is the brief instruction on how to install R package "arayQualityMetrics" in Debian.    

```R
# install the graphics library cairo
sudo apt-get install libcairo2-dev
# install X toolkit intrinsiscs development files
sudo apt-get install libxt-dev
# install development files for the Gnome XML library
sudo apt-get install libxml2-dev
# if you have installed BiocInstaller 
library(BiocInstaller)
biocLite('arrayQualityMetrics')
# if you haven't installed R package BiocInstaller
source("http://bioconductor.org/biocLite.R")
biocLite('arrayQualityMetrics')
```

Installing R package "arrayQualityMetrics" takes a while, so be patient. 

