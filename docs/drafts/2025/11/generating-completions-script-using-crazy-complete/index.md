---
title: "Generating Completions Script Using crazy-complete"
date: 2025-11-16 16:02:18
modified: 2025-11-18 03:23:46
authors:
  - bendu
label: generating-completions-script-using-crazy-complete
license: CC-BY-4.0
tags:
  - Computer Science
  - programming
  - shell
  - bash
  - zsh
  - fish
  - completion
  - generator
  - generating
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

There are many tools for generating completion scripts for shell languages (bash, zsh, fish, etc),
[crazy-complete](https://github.com/crazy-complete/crazy-complete)
is one of the best among such tools.

```
ldc -h | crazy-complete --input-type=help yaml /dev/stdin > ldc.yaml
crazy-complete --input-type=yaml fish ldc.yaml > ldc.fish
```

See
https://github.com/legendu-net/icon/tree/dev/completion
for a real example.

## References

- [crazy-complete @ GitHub](https://github.com/crazy-complete/crazy-complete)

