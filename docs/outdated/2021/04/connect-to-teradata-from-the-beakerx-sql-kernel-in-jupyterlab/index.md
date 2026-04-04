---
title: Connect to Teradata from the BeakerX SQL Kernel in JupyterLab
date: 2021-04-10 23:47:18
modified: 2021-02-10 23:47:18
authors:
- bendu
label: connect-to-teradata-from-the-beakerx-sql-kernel-in-jupyterlab
license: CC-BY-4.0
tags:
- programming
- Jupyter
- JupyterLab
- SQL
- BeakerX

---
**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**
You can run the following magics in a cell to connect to Teradata from a BeakerX SQL kernel.

    :::bash
    %classpath add jar /workdir/jars/teradata/tdgssconfig.jar
    %classpath add jar /workdir/jars/teradata/terajdbc4.jar
    %defaultDatasource jdbc:teradata://your.teradata.com/USER=your_username,PASSWORD=your_password

After connecting to a Teradata server,
you can write SQL code in a cell just like in any other SQL IDE.
