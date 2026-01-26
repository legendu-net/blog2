---
title: "Set Line Space in LaTeX"
date: 2012-11-13 00:05:22
modified: 2016-07-13 00:05:22
authors:
  - bendu
label: set-line-space-in-latex
license: CC-BY-4.0
tags:
  - LaTeX
  - programming
  - line
  - spacing
  - space
---


1. The `parskip` command makes a skip between paragraphs. 
The length of skip can be set using the command `\setlength`, e.g.,

        \setlength{\parskip}{15pt plus 1pt minus 1pt}

4. The command `\itemsep` sets the space between items in lists, e.g.,

        \begin{itemize}
        \itemsep = 0.8cm
        \item 
        \end{itemize}

3. The command `\doublespace` makes lines after this command double spaced. 
This is convenient to produce PDF document for review.

