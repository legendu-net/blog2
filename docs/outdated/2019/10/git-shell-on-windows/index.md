---
title: Git Shell on Windows
created: 2019-10-14 01:01:31
date: 2026-04-13 23:28:04.416052
authors:
  - bendu
label: git-shell-on-windows
license: CC-BY-4.0
tags:
  - software
  - Git
  - shell
  - Windows
  - WSL
  - Windows Subsystem Linux
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

\*\*
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
\*\*

It is suggested that you use Git in Windows Subsystem Linux (WSL)
instead of Git Shell in Windows.

1. git bash shell (on Windows) also uses shitf + insert to paste.

1. Git bash shell use /c, /d, /e, etc. for root path of drives.

1. It seems to me that
   `git config --global core.fileModel`
   has no effect on Windows.
   You can use `git -c core.fileMode=false command` as an alternative.

1. Git diff origin/master..HEAD

1. Git diff 15dc8^!
