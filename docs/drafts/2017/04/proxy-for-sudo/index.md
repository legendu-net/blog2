---
title: "Proxy for sudo"
date: 2017-04-07 23:42:48
modified: 2025-12-22 23:58:24
authors:
  - bendu
label: proxy-for-sudo
license: CC-BY-4.0
tags:
  - Network
  - proxy
  - environment variable
  - sudo
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

You can setup proxy in a terminal by export environment variables `http_proxy` and `https_proxy'.
```bash
export http_proxy='proxy_server:port'
export https_proxy='proxy_server:port'
```
However,
you might find the exported environment variables are not visible to `sudo`.
This can be resovled by simplying adding the `-E` (preserve environment) option to `sudo`.
```bash
sudo -E command_to_run
```

For more discussions,
please refer to
[Environment Variables and Secure Path for sudo]( https://www.legendu.net/misc/blog/environment-variables-and-secure-path-for-sudo )
.
