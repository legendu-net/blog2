---
title: Tips on ssh-keygen
created: 2024-03-12 16:36:40
date: 2026-04-13 23:14:24.627475
authors:
  - bendu
label: tips-on-ssh-keygen
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - SSH
  - ssh-keygen
  - key
  - generation
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Use the following command to generate new RSA keys without prompt questions.

```
ssh-keygen -q -y -t rsa -N '' -f ~/.ssh/id_rsa
```
