---
title: A Text File Is Marked as a Binary File
created: 2022-01-16 21:41:26
date: 2026-04-13 23:14:50.345053
authors:
  - bendu
label: a-text-file-is-marked-as-a-binary-file
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Linux
  - file
  - text
  - binary
  - null character
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

The issue can be fix by stripping null characters using the following command.

```
:::bash
tr -d '\000' < filein > fileout
```

## References

- [I'm having trouble with a text file being marked as a binary](https://superuser.com/questions/324867/im-having-trouble-with-a-text-file-being-marked-as-a-binary)
