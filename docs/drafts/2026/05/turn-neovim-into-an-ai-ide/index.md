---
title: Turn Neovim into An AI IDE
created: 2026-05-01 21:18:26.870750
date: 2026-05-02 09:02:16.627603
authors:
  - bendu
label: turn-neovim-into-an-ai-ide
license: CC-BY-4.0
tags:
  - editor
  - IDE
  - Neovim
  - avante
  - AI
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

[avante.nvim](https://github.com/yetone/avante.nvim)
is a Neovim plugin designed to emulate the behaviour of the Cursor AI IDE.
It provides users with AI-driven code suggestions
and the ability to apply these recommendations directly to their source files with minimal effort.

## Installation and Configuration via AstroNvim

1. Enable avante.nvim in
   [lua/community.lua](https://github.com/legendu-net/AstroNvim_template/blob/main/lua/community.lua#L10)
   .

1. Customize configuration (e.g., LLM provider) in
   [lua/plugins/avante.lua](https://github.com/legendu-net/AstroNvim_template/blob/main/lua/plugins/avante.lua)
   if needed.

1. Export API keys.
   Taking Gemini as an example,
   exporting either `GEMINI_API_KEY` or `AVANTE_GEMINI_API_KEY` (preferred) works.
   To do this in the fish shell,
   use

   ```fish
   set -Ux GEMINI_API_KEY "your_api_key_here"
   ```

   or

   ```fish
   set -Ux AVANTE_GEMINI_API_KEY "your_api_key_here"
   ```

   If you don't want like exporting environment variables for API keys (due to security concerns),
   you can manage your API keys using a password manager (e.g., pass)
   and have the following configuration in\
   [lua/plugins/avante.lua](https://github.com/legendu-net/AstroNvim_template/blob/main/lua/plugins/avante.lua)
   .

   ```
   gemini = {
       api_key_name = "cmd:pass show google/gemini-api",
   }
   ```

1. If you run into errors saying "cannot make changes. modifiable is off" when using the sidebar,
   run `:set modifiable` to toggle on modifiable.

## References

- [Avante.nvim Leader Key Configuration](https://gemini.google.com/share/75f7c0526efc)

- [Fix avante.nvim Build Error](https://gemini.google.com/share/7016ae809f58)
