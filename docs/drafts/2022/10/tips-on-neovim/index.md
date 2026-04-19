---
title: Tips on Neovim
created: 2022-10-16 19:54:05
date: 2026-04-18 00:37:03.788073
authors:
  - bendu
label: tips-on-neovim
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Neovim
  - IDE
  - PPA
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation Using Homebrew on Linux/macOS (Recommended)

```
brew install neovim
```

This is the recommended way to install Neovim.

## Installation Using AppImage

Just download the [AppImage](https://github.com/neovim/neovim/releases).
This can be a good choice if you want to install the latest version of NeoVim
but don't want to use a PPA (on Ubuntu)
and don't want to introduce a dependency on Homebrew.
For example,
when you build a Docker image and want to install the lateat version of Neovim for all users.

## Installation on Ubuntu

```
sudo apt update
sudo apt install neovim
```

Note that the Neovim installed might be an old version.
Use Homebrew of AppImage instead if you want a newer version of Neovim.

## Tips and Traps

1. [AstroNvim](https://github.com/AstroNvim/AstroNvim) is a great configuration for NeoVim.

1. NeoVim with a complicated configuration (e.g., AstroNvim, SpaceVim, etc)
   might be too slow when editing a large (>50M) text file.
   One trick helps is to disable plugins when editing large files.
   For example,
   you can use the following command to edit a large file without loading plugins.

   ```
    :::bash
    nvim --noplugin /path/to/large/text/file
   ```

## Manage Language Servers

### Python

```
:LspInstall ruff ty
```

## Repeat

- [Adding dot-repeat to your Neovim plugin](https://gist.github.com/kylechui/a5c1258cd2d86755f97b10fc921315c3)

- [Better repeat #1025](https://github.com/neovim/neovim/issues/1025)
