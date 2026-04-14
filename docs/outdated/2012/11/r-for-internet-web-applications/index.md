---
title: R for Internet/Web Applications
created: 2012-11-14 22:22:58
date: 2026-04-13 23:33:14.793449
authors:
  - bendu
label: r-for-internet-web-applications
license: CC-BY-4.0
tags:
  - email
  - R
  - web
  - programming
  - network
  - internet
  - CRAN
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

<img src="/media/r/r.png" height="200" width="240" align="right"/>

## Sending/Receiving Emails

1. There are many ways to send email in R.
   First, you can use `sendmail{sendmailR}`.
   The following code is a simple test email.

   ```
    sendmail(from="firedragon.du@gmail.com",
    to="dclong@iastate.edu",
    subject="Sending Email from R",msg="It works",
    control=list(smtpServer="mailhub.iastate.edu"))
   ```

   In this way, you can attach objects in R directly to the email,
   but it does not support email authentication,
   and it does not support multiple recipients very well.
   Second, you can call code written in other languages in R to send emails.
   For example,
   you can use `rJava` to call Java code to send emails in R.
   I have written an R package [dclong.jmail](https://github.com/dclong/dclong.spt)
   based on Java Mail API
   which can be used to send/receive emails.
   It supports email authentication.
   Another way is to use `system` or `shell`
   to call executable applications to send emails.
   There are many such email applications in Linux system.
   For Windows system,
   the application `sendEmail` written by Brandon zehm is good one,
   which support Gmail, multiple recipients and multiple attachments.

## Automated Web Browsing

1. RCurl/httr/XML

1. download.file
