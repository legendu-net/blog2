---
title: "Maning Packages Using Yum in CentOS"
date: 2017-04-22 15:41:55
modified: 2020-05-22 15:41:55
authors:
  - bendu
label: yum-tips
license: CC-BY-4.0
tags:
  - Linux
  - yum
  - rpm
  - RedHat
  - CentOS
  - package management
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```bash
yum update

yum search vim

yum install yum-utils

yum install pkg

yum localinstall pkg

yum groupinstall development

yum install https://centos7.iuscommunity.org/ius-release.rpm

yum info unixODBC 

rpm -ivh pkg.rpm
rpm -qa
rpm -qa | grep -i odbc
```

## Proxy

[Using yum with a Proxy Server](https://docs.fedoraproject.org/en-US/Fedora_Core/3/html/Software_Management_Guide/sn-yum-proxy-server.html)

