---
title: "Make Plots in SAS"
date: 2012-07-11 00:00:00
modified: 2012-07-11 00:00:00
authors:
  - bendu
label: sas-plot
license: CC-BY-4.0
tags:
  - image
  - SAS
  - graphics
  - programming
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

<img src="http://dclong.github.io/media/sas/sas.jpg" height="200" width="240" align="right"/>

2. There are functions to add points, lines and legends to an existing plot in R.
In SAS, there is no way to do this. 
What you can do is to add plotting commands in the plotting procedure and rerun your code. 

3. Staring from version 9.2, SAS offers new procedures such as PROC SGPLOT and PROC SGPANEL for making plots.
PROC SGPLOT (sophisticated graphical plot) produces high quality plots. 
PROC SGPANEL divides the window into several parts and make plots on these sub area.

4. It is possible to call R from SAS which means that you can use R to make plots in SAS if you like. 
