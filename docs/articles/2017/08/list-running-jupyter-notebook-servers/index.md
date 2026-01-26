---
title: "List Running Jupyter Notebook Servers"
date: 2017-08-22 12:21:29
modified: 2017-10-22 12:21:29
authors:
  - bendu
label: list-running-jupyter-notebook-servers
license: CC-BY-4.0
tags:
  - software
  - notebook
  - Jupyter Notebook
  - JupyterLab
  - Python
  - root
  - running servers
  - list
---

You can list running Jupyter Notebook servers using the following command.

    jupyter notebook list

It works well most of the time. 
However, 
if the servers are launched using the root account (e.g., in a Docker container), 
you might encounter issues. 
In this case,
a better alternative is to list running servers using Python script.

    from notebook import notebookapp
    servers = list(notebookapp.list_running_servers())
    print servers

For more please refer to 
<https://stackoverflow.com/questions/41782255/how-to-get-the-current-jupyter-notebook-servers-in-python>.


