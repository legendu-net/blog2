---
title: Navigate Chrome Browser Like a Pro Using Vimium
created: 2014-12-18 15:05:35
date: 2026-04-19 21:16:59.854672
authors:
  - bendu
label: navigate-chrome-browser-like-a-pro-using-vimium
license: CC-BY-4.0
tags:
  - software
  - Chrome
  - Vimium
  - Vim
  - plugin
  - add-on
  - addon
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```{note}
There are apps for navigate any GUI applications (instead of just for browser).
See
[Navigate GUI Applications Without Mouse in Linux](navigate-gui-applications-without-mouse-in-linux)
for more discussions.
```

## Customize Key Mappings

1. Open Vimium Options.

1. Paste your customized key mappings into "Custom key mappings".
   Below is an example of my customized key mapping configuration.

   ```sh
   map d removeTab
   map u restoreTab
   unmap x
   unmap X
   map <c-d> scrollPageDown
   map <c-u> scrollPageUp
   map <c-f> scrollFullPageDown
   map <c-b> scrollFullPageUp
   ```

1. Click the "Save changes" button at the bottom-left corn.

## Alternatives

- [Navigate GUI Applications Without Mouse in Linux](navigate-gui-applications-without-mouse-in-linux)

- [Anything better than SurfingKeys?](https://www.reddit.com/r/vim/comments/qbo35r/anything_better_than_surfingkeys/)

- [Surfingkeys @ GitHub](https://github.com/brookhong/Surfingkeys)

- [Tridactyl and Surfingkeys are Vimium on Steroids](https://devctrl.blog/posts/tridactyl-surfingkeys-vimium-on-steroids/)
