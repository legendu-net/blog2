---
title: Tips on fd
created: 2025-06-15 20:40:23
date: 2026-04-13 23:14:19.773183
authors:
  - bendu
label: tips-on-fd
license: CC-BY-4.0
tags:
  - computer science
  - fd
  - fdfind
  - Linux
  - shell
  - find
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips & Traps

1. `fd` is much faster compared to `find`.

## Installation

```
sudo apt install fd-find
```

The install binary is `fdfind`.

## Example Usages

1. Find all directories under `$dir`.

   ```
    fdfind --type d . $dir 
   ```

1. Find all files under `$dir`.

   ```
    fdfind --type f --print0 . $dir 
   ```

## References

- [fd @ GitHub](https://github.com/sharkdp/fd)
