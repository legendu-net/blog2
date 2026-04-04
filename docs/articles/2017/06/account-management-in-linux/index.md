---
title: "Account Management in Linux"
created: 2017-06-22 13:30:05
date: 2017-10-22 13:30:05
authors:
  - bendu
label: account-management-in-linux
license: CC-BY-4.0
tags:
  - Linux
  - account management
  - group managment
  - adduser
  - useradd
  - gpasswd
  - getent
---

**
Things on this page are
fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Create a User 

Both `adduser` and `useradd` can be used to create a new user. 
`adduser` is interactive while `useradd` is non-interactive.
It is suggested that you use `useradd` in batch mode
and `adduser` in non-batch mode.

```sh
useradd -o -m -u -g -d 
groupadd -o -g 
```

## Group

Add a user to a group.
```sh
gpasswd -a user_name group_name
```

Get information about a group.
```sh
getent group group_name
getent group group_id
```
