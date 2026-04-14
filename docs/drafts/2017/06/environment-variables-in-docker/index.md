---
title: Environment Variables in Docker
created: 2017-06-07 21:47:47
date: 2026-04-13 23:33:10.309592
authors:
  - bendu
label: environment-variables-in-docker
license: CC-BY-4.0
tags:
  - software
  - Docker
  - shell form
  - exec form
  - environment variable
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Environment Variables

1. It seems that Docker reads neither `/etc/profile`
   nor `/etc/environment` for environment variables.
   For more details,
   please refer to the issue
   [setting environment variables in a docker container #25388](https://github.com/moby/moby/issues/25388)
   on GitHub.

1. You can create environment variables for the current user
   using the command `ENV`.
   And you can also manually export environment variables in a init script once the container is started.

1. There is an option in JupyterHub to keep env virables
   from the JupyterHub process for JupyterLab processes.

## Environment Variables in Entrypoint

The exec form of ENTRYPOINT does not invoke a command shell,
unlike the shell form.
This means that normal shell processing does not happen for exec form.
For example,
`ENTRYPOINT [ "echo", "$HOME" ]` will not do variable substitution on `$HOME`.
If you want shell processing then either use the shell form
or execute a shell directly,
e.g.,
`ENTRYPOINT [ "sh", "-c", "echo", "$HOME" ]`.
When using the exec form and executing a shell directly,
as in the case for the shell form,
it is the shell that is doing the environment variable expansion, not docker.
