---
title: "Install NodeJS on Ubuntu"
created: 2017-07-07 12:12:37
date: 2020-03-07 12:12:37
authors:
  - bendu
label: install-nodejs-on-ubuntu
license: CC-BY-4.0
tags:
  - software
  - NodeJS
  - installation
  - Ubuntu
  - node
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

    :::bash
    wajig install nodejs npm
    sudo ln -s /usr/bin/nodejs /usr/bin/node

Notice that it is necessary to create a symbolic link for node, 
as many Node.js tools use this name to execute.

## References

[How to Install Latest Node.js and NPM on Ubuntu with PPA](https://tecadmin.net/install-latest-nodejs-npm-on-ubuntu/)