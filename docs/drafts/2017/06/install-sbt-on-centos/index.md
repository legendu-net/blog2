---
title: "Install sbt on CentOS"
date: 2017-06-25 10:37:51
modified: 2017-06-25 10:37:51
authors:
  - bendu
label: install-sbt-on-centos
license: CC-BY-4.0
tags:
  - Linux
  - CentOS
  - RedHat
  - sbt
  - install
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```sh
wget http://dl.bintray.com/sbt/rpm/sbt-0.13.5.rpm
sudo yum install sbt-0.13.5.rpm
```

```sh
curl https://bintray.com/sbt/rpm/rpm | sudo tee /etc/yum.repos.d/bintray-sbt-rpm.repo
sudo yum install sbt
```
