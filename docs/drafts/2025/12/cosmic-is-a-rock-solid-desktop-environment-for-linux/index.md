---
title: COSMIC Is a Rock Solid Desktop Environment for Linux
created: 2025-12-22 10:34:27
date: 2026-04-13 23:14:17.810348
authors:
  - bendu
label: cosmic-is-a-rock-solid-desktop-environment-for-linux
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Linux
  - desktop
  - COSMIC
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Auto Login

/etc/greetd/cosmic-greeter.toml

```
[terminal]
vt = "1"

[general]
service = "login"

[default_session]
command = "cosmic-greeter-start"
user = "cosmic-greeter"

[initial_session]
command = "start-cosmic"
user = "username"
```

https://github.com/pop-os/cosmic-greeter/issues/80
