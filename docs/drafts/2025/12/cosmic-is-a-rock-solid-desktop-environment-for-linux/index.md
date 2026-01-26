---
title: "COSMIC Is a Rock Solid Desktop Environment for Linux"
date: 2025-12-22 10:34:27
modified: 2025-12-22 17:42:56
authors:
  - bendu
label: cosmic-is-a-rock-solid-desktop-environment-for-linux
license: CC-BY-4.0
tags:
  - Computer Science
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
