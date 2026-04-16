---
title: Shell in Docker
created: 2020-06-21 10:46:43
date: 2026-04-15 19:27:01.015223
authors:
  - bendu
label: shell-in-docker
license: CC-BY-4.0
tags:
  - computer science
  - Docker
  - shell
  - container
  - Bash
  - RUN
  - ENV
  - environment variable
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Configure the Shell for the `RUN` Command

https://docs.docker.com/engine/reference/builder/#shell

## Configure the Default Shell for Terminals in Docker Containers

Just set the SHELL environment variable in the Docker image.

```
:::bash
ENV SHELL=/bin/bash
```
