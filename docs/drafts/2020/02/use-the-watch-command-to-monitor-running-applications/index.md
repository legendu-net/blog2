---
title: Use the Watch Command to Monitor Running Applications
created: 2020-02-17 13:13:30
date: 2026-04-14 19:32:04.559306
authors:
  - bendu
label: use-the-watch-command-to-monitor-running-applications
license: CC-BY-4.0
tags:
  - programming
  - shell
  - Linux
  - watch
  - monitor
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Report the number of PNG images in the directory `000` every 2 seconds.

```
:::bash
watch "ls 000/*.png | wc -l"
```
