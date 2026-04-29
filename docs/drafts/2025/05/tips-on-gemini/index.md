---
title: Tips on Gemini
created: 2025-05-06 15:04:36
date: 2026-04-28 20:02:53.077852
authors:
  - bendu
label: tips-on-gemini
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - AI
  - Gemini
  - Google
  - cookbook
  - prompt
  - studio
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## General Tips

1. The YOLO mode (`gemini --yolo`) is strongly discouraged.
   It is suggested that you leverage
   [Policy Engine](https://geminicli.com/docs/reference/policy-engine/)
   to grant permissions for each specific tool.

1. Google Gemini saves conversations and apps you built so that you can revisit them later.
   Notice that prompts (conversations) are also saved into
   the directory "My Drive/Google AI Studio" in your Google drive.

## Gemini Custom Commands vs Skills

Skills are preferred to custom commands for a few reasons.

1. Skill is open standard and is portable to other agents (Claude, Codex, etc).

1. A custom command can be implemented as a skill.

1. It's easier and more flexible to trigger a skill (though mismatch might happen).

## Gemini Extensions

Gemini supports extensions
(similar concepts to [Claude Plugins](https://claude.com/plugins))
.

- [Official Gemini Extension Market](https://geminicli.com/extensions/)

- [More Gemini Extensions](https://github.com/gemini-cli-extensions)

## Automation Workflows Based on Gemini CLI

[Automate tasks with headless mode](https://geminicli.com/docs/cli/tutorials/automation/)

## Update on All Things of Gemini

- [Gemini App](https://blog.google/innovation-and-ai/products/gemini-app/)

- [Gemini Drops](https://gemini.google/gemini-drops/)

- [Try notebooks in Gemini to easily keep track of projects](https://blog.google/innovation-and-ai/products/gemini-app/notebooks-gemini-notebooklm/)

## Google's AI Studio

- Based on Gemini.
- Best for prototyping and building apps.
- Publish an app or not once you are satisfied with it?
  - Without publishing, you have to rebuild it often which is time consuming and can be annoying.
  - Publishing an app will make it accessible to public by default
    which exposes yourself to the risk of letting random people use your app and consume your token quota.
    A possible setup is to publish the app (to Google Cloud Run)
    but configure Google Cloud Run to be accessible only by yourself.
    .

## References

- [Tips on Google Gemini CLI](tips-on-google-gemini-cli)

- [Automated Browsing Tasks Using Gemini in Chrome](automated-browsing-tasks-using-gemini-in-chrome)

- [Gemini API Cookbook](https://github.com/google-gemini/cookbook)

- [Google AI Studio](https://aistudio.google.com/prompts/new_chat)

- [Tips on Google Gemini Cli](https://www.legendu.net/misc/blog/tips-on-google-gemini-cli)
