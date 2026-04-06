---
title: Add Users to a Group in Linux
created: 2016-06-10 19:05:41
date: 2026-04-05 19:42:37.438087
authors:
- bendu
label: add-users-to-a-group-in-linux
license: CC-BY-4.0
tags:
- Linux
- sudo
- user
- groups
- gpasswd
- usermod
---
There are several ways to add users to a group in Linux. 
The following uses the `sudo` group as illustration.

1. `gpasswd`, `usermod` and `adduser` can all be used to add a user to a given group.
    However, it is suggested that you use `gpasswd` as it is more portable and intuitive. 

        gpasswd -a user_name sudo
        newgrp sudo

        usermod -aG sudo user_name
        newgrp sudo

        # works on Ubuntu but not CentOS
        adduser user_name sudo
        newgrp sudo

    Just adding an user to a group might not make it work right away.
    The command `newgrp sudo` make the group `sudo` in effect right away.
    Of course, you can log out and then log in to make it work.

3. Some desktop environment (e.g., GNome, Cinnamon, KDE, etc.) can also do this for you. 
    Taking Cinnamon as an example, 
    you can follow the steps below to add/remove groups for a user. 

    1. Open `System Settings`.

    2. Click `Users and Groups`.

    3. Select the user you want modify.

    3. Click on `Groups`.

    4. Check/uncheck groups from the prompt list.

    5. Click the OK to save the changes.
