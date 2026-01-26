---
title: "Regular Expression in Bash"
date: 2019-04-28 11:53:55
modified: 2021-10-27 20:23:31
authors:
  - bendu
label: regular-expression-in-bash
license: CC-BY-4.0
tags:
  - programming
  - Bash
  - regular expression
  - regex
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**


[Fish Shell]( https://www.legendu.net/misc/blog/tips-on-the-fish-shell ) 
is preferred to Bash/Zsh.
The following content is for Bash/Zsh only.

It is suggested that you **use Python script instead of Shell script** as much as possible.
If you do have to stick with Shell script,
you can use `=~` for regular expression matching in Bash.
This make Bash syntax extremely flexible and powerful.
For example, 
you can match multiple strings using regular expression.
```
if [[ value =~ ^(v1|v2|v3)$ ]]; then
    ...
fi
```
