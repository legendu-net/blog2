---
title: "The Checkbutton Widget in Tkinter"
created: 2020-04-12 21:57:28
date: 2021-08-08 16:25:26
authors:
  - bendu
label: the-checkbutton-widget-in-tkinter
license: CC-BY-4.0
tags:
  - Computer Science
  - Python
  - programming
  - Tkinter
  - GUI
  - Checkbutton
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


1. `ttk.Checkbutton` is preferred to `tk.Checkbutton`.

2. It seems to me that the `Checkbutton.bind` doesn't work.
    However, 
    specifying a callback function using the `command` option 
    when creating a Checkbutton still work.
