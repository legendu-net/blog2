---
title: "Resolve the DNS Contamination Issue in Firefox"
date: 2018-09-11 01:11:28
modified: 2021-09-26 21:54:44
authors:
  - bendu
label: resolve-the-dns-contamination-issue-in-firefox
license: CC-BY-4.0
tags:
  - software
  - Firefox
  - proxy
  - DNS contamination
  - socks
---

The local DNS you use in China is probably contaminated
and popular sites like Google, Facebook, etc. are not interpreted correctly.
So if you are in China and use Firefox with Proxy,
make sure to set `network.proxy.socks_remote_dns` to be true (follow steps below).

1. Open an empty tab in Firefox.

2. Go to about:config in the URL bar.

3. Search for `network.proxy.socks_remote_dns`.

4. Change the value to be `true`.
