---
title: "Speed Up sbt in China"
created: 2017-08-22 12:39:58
date: 2017-10-22 12:39:58
authors:
  - bendu
label: speed-up-sbt-in-China
license: CC-BY-4.0
tags:
  - programming
  - sbt
  - Scala
  - proxy
  - HTTP
  - socks
  - repository
  - proxy repository
  - China
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

Currently `sbt` uses https by default. 
However, the Great Firewall of China makes https visits to websites out of China slow. 

## Proxy

If you have access to proxy server, 
it is probably the most convenient way. 

1.  HTTP Proxy

        export JAVA_OPTS="$JAVA_OPTS -Dhttp.proxyHost=yourserver -Dhttp.proxyPort=8080 -Dhttp.proxyUser=username -Dhttp.proxyPassword=password"
        sbt 

2. Socks Proxy 

        sbt -DsocksProxyHost=proxy_ip -DsocksProxyPort=port 

## Repository Mirror (Proxy Repository)

`sbt` uses Ivy to resolve library dependencies. 
However, 
unlike Gradle `sbt` does NOT inherit Maven configurations. 
You have to configure `sbt` separately. 
It is really easy to set up proxy repositories for `sbt`. 
All you have to do is to add the following section into the file 
`~/.sbt/repositories`.

    [repositories]
        local
        aliyun: http://maven.aliyun.com/nexus/content/groups/public/
        central: http://repo1.maven.org/maven2/

The repositories are used in the order local > aliyun > central. 
You can add other repositories similarly (using the ke: value format). 
[Ali Maven Mirror](http://maven.aliyun.com/nexus/#welcome) 
is great for use in China.


