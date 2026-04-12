---
title: Tips on Jupyter-Book
created: 2020-09-20 14:47:06
date: 2026-04-03 23:58:36.930768
authors:
- bendu
label: tips-on-jupyter-book
license: CC-BY-4.0
tags:
- Computer Science
- jupyter-book
- Markdown
- notebook
- Jupyter
- JupyterLab
- blog
---
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

icon jb -ic

[MyST Markdown Sandbox](https://mystmd.org/sandbox)

## Configuration 

`icon jb -c` creates a copy of configuration file `_config.yml` in the current directory.
By default,
The configuration file `_config.yml` in the current directory (if exists) is used.
So `jb build --config _config.yml *.ipynb` is equivalent to `jb build *.ipynb`.

## Blogging

[myst example](https://github.com/jupyter-book/blog/blob/main/docs/myst.yml)

https://github.com/jupyter-book/example-landing-pages

https://mystmd.org/guide/frontmatter

https://mystmd.org/guide/glossaries-and-terms#abbreviations sounds interesting!

NODE_OPTIONS=--max-old-space-size=8192 uv run jupyter-book start



### Themes

It seems to me that public themes 
(e.g., https://github.com/QuantEcon/quantecon-book-theme)
are not supported currently.

## References 

- [Jupyter Book 101: Beautiful, publication-quality documents from computational material](https://www.youtube.com/watch?v=lZ2FHTkyaMU)

- [jupyter-book - Official Doc](https://jupyterbook.org/intro.html)

- [jupyter-book @ GitHub](https://github.com/executablebooks/jupyter-book)

- [The command-line interface](https://jupyterbook.org/reference/cli.html?highlight=verbose#the-command-line-interface)

- [Build Your Book](https://jupyterbook.org/start/build.html)

- [Configure book settings](https://jupyterbook.org/customize/config.html?highlight=timeout)

- [Hide or remove content](https://jupyterbook.org/interactive/hiding.html?highlight=hide%20code#hide-or-remove-content)

- [Execute and cache your pages](https://jupyterbook.org/content/execute.html?highlight=timeout)
