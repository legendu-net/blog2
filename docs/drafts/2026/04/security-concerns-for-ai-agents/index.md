---
title: Security Concerns for AI Agents
created: 2026-04-28 22:36:04.593440
date: 2026-04-28 22:36:04.593442
authors:
  - bendu
label: security-concerns-for-ai-agents
license: CC-BY-4.0
tags:
  - AI
  - agent
  - security
  - vulnerability
  - prompt injection
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## [code-on-incus (COI)](https://github.com/mensfeld/code-on-incus)
[code-on-incus (COI)](https://github.com/mensfeld/code-on-incus)
gives each AI agent its own machine - a full system container with root access, systemd, Docker, and the ability to install anything. 
Agents work like they would on a real server: run services, manage packages, use cron - without touching your actual system. 
Files stay correctly owned, no permission hacks needed.


https://github.com/anthropics/skills/pull/557
feat: add security-scanning skill for LLM safety guardrails


https://repello.ai/blog/ai-agent-skill-scanner
 AI Agent Skill Scanners: Every Tool Compared (2026)


Cisco skill-scanner

SkillCheck (Repello)

https://skillforge-tawny.vercel.app/scanner

