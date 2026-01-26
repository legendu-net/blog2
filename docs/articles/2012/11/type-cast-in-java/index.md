---
title: "Type Cast in Java"
date: 2012-11-02 10:50:55
modified: 2014-10-02 10:50:55
authors:
  - bendu
label: type-cast-in-java
license: CC-BY-4.0
tags:
  - type cast
  - programming
  - Java
---


1. You cannot cast between integer and boolean values. 
However it is trivia to convert data between integer and boolean. 
For example,
`int i = b ? 1 : 0;` convert a boolean value `b` into an integer value `i`, 
and `boolean b = i != 0` convert an integer value `i` into a boolean value `b`.
