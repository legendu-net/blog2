---
title: List Running Jupyter Notebook Servers
created: 2017-08-22 12:21:29
date: 2026-04-15 19:27:00.417273
authors:
  - bendu
label: list-running-jupyter-notebook-servers
license: CC-BY-4.0
tags:
  - software
  - notebook
  - Jupyter
  - JupyterLab
  - Python
  - root
  - running servers
  - list
---

You can list running Jupyter Notebook servers using the following command.

```
jupyter notebook list
```

It works well most of the time.
However,
if the servers are launched using the root account (e.g., in a Docker container),
you might encounter issues.
In this case,
a better alternative is to list running servers using Python script.

```
from notebook import notebookapp
servers = list(notebookapp.list_running_servers())
print servers
```

For more please refer to
<https://stackoverflow.com/questions/41782255/how-to-get-the-current-jupyter-notebook-servers-in-python>.
