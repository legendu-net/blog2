---
title: "Check Whether an Email Address Is Valid in Java"
date: 2012-05-12 23:58:54
modified: 2016-07-12 23:58:54
authors:
  - bendu
label: valid-email-address-java
license: CC-BY-4.0
tags:
  - pattern
  - match
  - Java
  - programming
  - email address
---

See the following code.

```Java
String email = "test@test.com";
Pattern p = Pattern.compile(".+@.+\\.[a-z]+");
Matcher m = p.matcher(email);
boolean matchFound = m.matches();
if(matchFound){
    System.out.println("EMAIL OK");
}else{
    System.out.println("EMAIL ERROR");
}
```
