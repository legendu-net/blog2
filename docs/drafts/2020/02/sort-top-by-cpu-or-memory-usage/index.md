---
title: Sort top by CPU or Memory Usage
created: 2020-02-18 11:56:57
date: 2026-04-15 19:27:01.075348
authors:
  - bendu
label: sort-top-by-cpu-or-memory-usage
license: CC-BY-4.0
tags:
  - OS
  - Linux
  - top
  - macOS
  - CPU
  - memory
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

By default the result of the `top` command is sorted by CPU usage on Linux.
The table below list options to sort the result of the `top` command
by different criterias on Linux and macOS

|                      | Linux       | macOS      |
| -------------------- | ----------- | ---------- |
| Sort by CPU usage    | top         | top -o cpu |
| Sort by Memory usage | top -o %MEM | top -o mem |

Note: The above table is generated with the help of [TableConvert Online](https://tableconvert.com/).
