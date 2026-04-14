---
title: Get Coordinates of Points on a Screen or Image
created: 2020-02-09 12:03:40
date: 2026-04-13 23:27:59.764196
authors:
  - bendu
label: get-coordinates-of-points-on-a-screen-or-image
license: CC-BY-4.0
tags:
  - software
  - coordinate
  - point
  - macOS
  - GIMP
  - image
  - screen
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Get the Coordinate of a Pixle/Point on an Image

Most image editing software (e.g., [GIMP](https://www.gimp.org/)) can tell you the coordinate of a point on an image.

## Get the Coordinate of a Pixle/Point on the Screen in macOS

`Shift + Command + 4` shows the coordinate of the current position of the mouse point.
Notice that the coordinate shown by `Shift + Command + 4`
need to be **multiplied by 2**
if you use Python packages (Pillow, pyscreenshot, etc.) to take screenshots.
