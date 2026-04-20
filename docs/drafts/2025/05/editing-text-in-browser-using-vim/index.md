---
title: Editing Text in Browser Using Vim
created: 2025-05-30 07:50:43
date: 2026-04-15 19:27:00.577227
authors:
  - bendu
label: editing-text-in-browser-using-vim
license: CC-BY-4.0
tags:
  - computer science
  - text
  - editing
  - editor
  - Vim
  - Neovim
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```{list-table} Firenvim Alternatives Summary
:header-rows: 1

- - Tool
  - How it Works
  - Pros
  - Cons
  - Best For...
  - Development
- - [withExEditor](https://github.com/asamuzaK/withExEditor)
  - 
  - 
  - Firefox only. 
  - 
  - Active 
- - [Firenvim](https://github.com/glacambre/firenvim)
  - Embeds a real Neovim instance
  - Full power of Neovim, embedded directly in the page.
  - Can be complex to set up, slightly higher resource usage.
  - Users who want a no-compromise, embedded Neovim experience.
  - Slow
- - [GhostText](https://github.com/fregante/GhostText)
  - External Editor (Real-time sync)
  - **Your full Neovim config**, real-time sync, multi-editor support.
  - Not embedded; requires a separate terminal window.
  - Users who prioritize the full power of their config over an embedded feel.
  - Inactive
- - [Textern](https://github.com/jlebon/textern)
  - External Editor (Save & Close)
  - **Your full Neovim config**, simple and robust.
  - Sync is not real-time, feels less integrated.
  - Firefox users or those wanting a simple "edit in external app" button.
  - Inactive
- - [Wasavi](https://github.com/akahuku/wasavi)
  - JS-based Vim Emulator
  - Excellent vi/Vim emulation, self-contained, no setup.
  - **No access to your Neovim config/plugins.**
  - Users who want a powerful Vim editing experience without needing their specific plugins.
  - Dead
- - **Vimium-C / Tridactyl / Surfingkeys**
  - Navigation with basic editing
  - All-in-one navigation and simple editing, very lightweight.
  - Editing capabilities are very limited.
  - Users whose primary goal is browser navigation, with text editing as a nice bonus.
```

## References

- [FireNVim Brings NeoVim into Your Browser](firenvim-brings-neovim-into-your-browser)

- [Use neovim in Google Chrome / Chromium through Surfingkeys](https://www.youtube.com/watch?v=Sff0fm-d6Vk)
