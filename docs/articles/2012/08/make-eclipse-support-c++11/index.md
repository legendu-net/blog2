---
title: Make Eclipse Support C++11
created: 2012-08-20 00:00:00
date: 2026-04-05 19:42:37.306240
authors:
- bendu
label: make-eclipse-support-c++11
license: CC-BY-4.0
tags:
- C/C++
- software
- eclipse
---
<img src="http://dclong.github.io/media/eclipse/cdt.png" height="200" width="240" align="right"/>

1. Make a new C++ project

1. Default options for everything

2. Once created, right-click the project and go to "Properties"

3. C/C++ Build -> Settings -> Tool Settings -> GCC C++ Compiler -> Miscellaneous -> Other Flags. 
Put -std=c++0x at the end. 

4. C++ General -> Paths and Symbols -> Symbols -> GNU C++. 
Click "Add..." and paste `__GXX_EXPERIMENTAL_CXX0X__` (ensure to append and prepend two underscores) 
into "Name" and leave "Value" blank.

5. Hit Apply, do whatever it asks you to do, then hit OK.

