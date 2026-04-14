---
title: GPU for Web
created: 2021-05-12 09:26:51
date: 2026-04-13 23:15:02.396190
authors:
  - bendu
label: gpu-for-web
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - GPU
  - Web
  - gpuweb
  - wgpu
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://github.com/gpuweb/gpuweb
This is the repository for the W3C's GPU for the Web Community Group.

## [gfx-rs](https://github.com/gfx-rs/gfx)

[gfx-rs](https://github.com/gfx-rs/gfx)
is a low-level, cross-platform graphics and compute abstraction library in Rust.
[gfx-rs](https://github.com/gfx-rs/gfx)
is hard to use.
It's recommended for performance-sensitive libraries and engines.
wgpu-rs is a safe and simple alternative.

## [wgpu](https://github.com/gfx-rs/wgpu)

[wgpu](https://github.com/gfx-rs/wgpu)
is an implementation of WebGPU API in Rust,
targeting both native and the Web.
See the upstream WebGPU specification (work in progress).

## [wgpu-py](https://github.com/pygfx/wgpu-py)

[wgpu-py](https://github.com/pygfx/wgpu-py)
is a next generation GPU API for Python.
It is a Python lib wrapping wgpu-native and exposing it with a Pythonic API similar to the WebGPU spec.

## References

[Point of WebGPU on native](http://kvark.github.io/web/gpu/native/2020/05/03/point-of-webgpu-native.html)
