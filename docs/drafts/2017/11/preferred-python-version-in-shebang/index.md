---
title: "Preferred Python Version in Shebang"
created: 2017-11-17 19:15:35
date: 2019-02-17 19:15:35
authors:
  - bendu
label: preferred-python-version-in-shebang
license: CC-BY-4.0
tags:
  - programming
  - shell
  - Python
  - shebang
  - version
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**



```
#!/bin/sh
''''which python2 >/dev/null 2>&1 && exec python2 "$0" "$@" # '''
''''which python  >/dev/null 2>&1 && exec python  "$0" "$@" # '''
''''exec echo "Error: I can't find python anywhere"         # '''
```

## Reference

https://stackoverflow.com/questions/18993438/shebang-env-preferred-python-version
