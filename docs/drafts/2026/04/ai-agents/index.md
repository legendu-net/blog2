---
title: AI Agents
created: 2026-04-16 09:42:35.777036
date: 2026-04-27 23:03:15.717500
authors:
  - bendu
label: ai-agents
license: CC-BY-4.0
tags:
  - AI
  - agent
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

At its simplest,
an AI Agent is a step up from a standard chatbot.
While a chatbot is designed to talk, an agent is designed to act.
Think of it like the difference between a travel guide who tells you about Paris (Chatbot)
and a personal assistant who actually books your flights, reserves the hotel, and handles the dinner reservations (Agent).

## The Core Components

An AI agent doesn't just respond to a prompt.
It follows a loop of reasoning to accomplish a goal.
Most agents operate using these four pillars.

- Perception: Taking in data from the environment (user prompts, web searching, or file reading).

- Brain (Reasoning): Using a Large Language Model (LLM) to break a complex goal into smaller, logical steps.

- Memory: Remembering past interactions or storing information found during a task to use later.

- Tools: The ability to "handshake" with other software (like your email, calendar, or a web browser) to execute actions.

## How it Works: The "Loop"

Unlike a single-turn conversation,
an agent often works in an autonomous loop until the job is done.

- Goal Setting: You give the agent a high-level objective (e.g., "Research the best laptop under \$1,000 and email a summary to my boss").

- Planning: The agent decides it needs to search the web, compare specs, and then access your email tool.

- Action: It executes the search and reads the results.

- Self-Correction: If the first search doesn't work, it tries a different query.

- Completion: It sends the email and notifies you it's finished.

## References

- [obra/smallest-agent](https://github.com/obra/smallest-agent)

- [Startup technical guide - AI agents](https://services.google.com/fh/files/misc/startup_technical_guide_ai_agents_final.pdf)
