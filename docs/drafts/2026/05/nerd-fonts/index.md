---
title: Nerd Fonts
created: '2026-05-24T21:03:48.778004-07:00'
date: '2026-05-25T13:27:24-07:00'
authors:
  - bendu
label: nerd-fonts
license: CC-BY-4.0
tags:
  - font
  - nerd
  - glyphs
  - icon
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://www.nerdfonts.com/

https://github.com/ryanoasis/nerd-fonts

Nerd Fonts is a project that patches developer targeted fonts with a high number of glyphs (icons). Specifically to add a high number of extra glyphs from popular 'iconic fonts' such as Font Awesome, Devicons, Octicons, and others.

https://github.com/ryanoasis/nerd-fonts#font-installation

Clone the project. Run ./install.sh.

## Configure JupyterLab Terminal to Use a Nerd Font

Set `fontFamily` to the desired nerd font in
`~/.jupyter/lab/user-settings/@jupyterlab/terminal-extension/plugin.jupyterlab-settings`
.

```json
{
    "fontFamily": "FiraCode Nerd Font",
    "fontSize": 13,
    "lineHeight": 1,
    "theme": "inherit",
    "screenReaderMode": false,
    "scrollback": 1000,
    "shutdownOnClose": false,
    "closeOnExit": true,
    "pasteWithCtrlV": true,
    "macOptionIsMeta": false,
    "cursorBlink": true,
    "showStatusBarItem": "if-any"
}
```
