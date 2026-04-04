---
title: "An Input Bug in Ruby"
created: 2012-08-06 11:28:52
date: 2020-04-06 11:28:52
authors:
  - bendu
label: input-bug-ruby
license: CC-BY-4.0
tags:
  - programming
  - Bash
  - Ruby
  - bug
  - terminal
  - IO
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

<img src="http://dclong.github.io/media/computer/bug.jpg" height="200" width="240" align="right"/>

If you run a ruby program though Bash 
and the ruby program read multiple inputs from the console, 
all inputs will be the same as the first argument. 
I'm not very sure how to solve this problem.

