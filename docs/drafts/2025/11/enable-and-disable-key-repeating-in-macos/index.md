---
title: Enable and Disable Key Repeating in macOS
created: 2025-11-27 01:05:39
date: 2026-04-13 23:14:18.404969
authors:
  - bendu
label: enable-and-disable-key-repeating-in-macos
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - macOS
  - Apple
  - keyboard
  - key
  - repeating
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. Run the following command in terminal and then **restart your Mac** to enable key repeating by pressing and holding.

   ```bash
    defaults write -g ApplePressAndHoldEnabled -bool false
   ```

1. Run the following command in terminal and then **restart your Mac** to disable key repeating by presing and holding.

   ```bash
    defaults write -g ApplePressAndHoldEnabled -bool true
   ```

For more details please refer to
[How to Enable Key Repeating in macOS](https://www.howtogeek.com/267463/how-to-enable-key-repeating-in-macos/)
.
