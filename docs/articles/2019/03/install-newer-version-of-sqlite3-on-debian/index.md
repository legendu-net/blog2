---
title: "Install Newer Version of SQLite3 on Debian Jessie"
date: 2019-03-10 10:27:02
modified: 2021-09-26 21:51:13
authors:
  - bendu
label: install-newer-version-of-sqlite3-on-debian
license: CC-BY-4.0
tags:
  - Linux
  - SQLite3
  - Debian
  - backports
  - SQLite
---


1. Open `/etc/apt/sources.list` and add the following line to the end.

        :::text
        deb http://www.backports.org/debian jessie-backports main contrib non-free

    or

        :::text
        deb http://ftp.us.debian.org/debian/ jessie-backports main contrib non-free
        deb-src http://ftp.us.debian.org/debian/ jessie-backports main contrib non-free

2. Make sure the GPG signatures are correct by running the following command.

        :::bash
        sudo apt-get update
        sudo apt-get install debian-backports-keyring

3. Install SQLite3.

        :::bash
        sudo apt-get update
        sudo apt-get -t jessie-backports install sqlite3 libsqlite3-dev
