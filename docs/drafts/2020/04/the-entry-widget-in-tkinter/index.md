---
title: The Entry Widget in Tkinter
created: 2020-04-12 21:56:51
date: 2026-04-13 23:15:23.601487
authors:
  - bendu
label: the-entry-widget-in-tkinter
license: CC-BY-4.0
tags:
  - computer science
  - Python
  - programming
  - Tkinter
  - GUI
  - Entry
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. `ttk.Entry` is preferred over `tk.Entry`.

1. `ttk.Entry`/`tk.Entry` does not have a `set` method to set the text directly.
   Instead,
   you have to first delete the text and then insert text into it.

   ```
    :::python
    entry.delete(0, tk.END)
    entry.insert(0, text)
   ```
