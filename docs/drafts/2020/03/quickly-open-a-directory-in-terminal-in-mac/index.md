---
title: Quickly Open a Directory in Terminal in Mac
created: 2020-03-11 16:25:01
date: 2026-04-15 19:27:01.061554
authors:
  - bendu
label: quickly-open-a-directory-in-terminal-in-mac
license: CC-BY-4.0
tags:
  - computer science
  - macOS
  - OpenInTerminal
  - terminal
  - hyper
  - iTerm
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

[OpenInTerminal](https://github.com/Ji4n1ng/OpenInTerminal)
is a `Finder Toolbar` app for macOS
to open the current or selected directory in Terminal, iTerm, Hyper or Alacritty.

## Installation and Configuration

1. Install OpenInTerminal

   ```
    :::bash
    brew cask install openinterminal
   ```

1. Launch OpenInTerminal from Applications.

1. An icon (looks like a terminal) will show up in the top bar.
   Click on it and chose "Open in terminal".
   A prompt will show up to ask you
   to select the default terminal application (Terminal, iTerm, Hyper, etc.)
   to use to open directories.

1. Once you've selected the default terminal application (to open directories),
   a prompt from Mac Security might show up
   to ask you whether to grant permission to the terminal application that you chose
   (if it hasn't been granted permission before).
   Please grant access to the terminal application.

1. Enable Finder Extension permission
   by going to System Preferences -> Extensions -> Finder Extensions
   and then checking the permission button.
   ![Finder Extension Permission](https://user-images.githubusercontent.com/824507/97831360-9ff7a580-1c84-11eb-80df-8ae2ddb3ee6d.png)
