---
title: Manage Password Using Gopass
created: '2026-05-25T19:31:05.793047-07:00'
date: '2026-05-30T20:53:13-07:00'
authors:
  - bendu
label: manage-password-using-gopass
license: CC-BY-4.0
tags:
  - gopass
  - password
  - management
  - token
  - key
  - age
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation on Fedora

```sh
sudo dnf install gopass age
```

## Initialization

```sh
gopass setup --crypto age --storage fs
```

which create an age identities file at\
`~/.config/gopass/age/identities`
.
The configuration file of gopass is at
`~/.config/gopass/config`
.

## Configuration for Git Sync

```sh
gopass config user.name "Your Name"
gopass config user.email "you@example.com"
gopass git init
gopass git remote add origin git@github.com:username/my-secrets-repo.git
```

`gopass` tracks the `master` branch of the Git repository.

## Configuration for Timeout

```sh
gopass config age.agent-enabled true
gopass config age.agent-timeout 900
```

## Manage Passwords

gopass insert api_keys/github

gopass show api_keys/github
