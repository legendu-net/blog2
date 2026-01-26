---
title: "Use Scala With Picocli"
date: 2019-06-22 03:41:22
modified: 2019-06-22 03:41:22
authors:
  - bendu
label: use-scala-with-picocli
license: CC-BY-4.0
tags:
  - programming
  - Scala
  - JVM
  - picocli
  - command-line interface
  - command-line parser
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

It is easy to make mistakes due to type of parameters when use picocli in Scala.
It is suggested that you

1. Have all parameters prepared before using them.

2. manually specify types of arguments when preparing parameters.

3. Never use `args("some-parameters")` directly. 
