---
title: Tips on Git Submodule
created: 2019-10-28 21:59:06
date: 2026-04-13 23:28:00.894855
authors:
  - bendu
label: tips-on-git-submodule
license: CC-BY-4.0
tags:
  - software
  - Git
  - submodule
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```bash
git submodule init
git submodule add git@github.com:dclong/docker_image_builder.git
git submodule update --recursive --remote
```

To remove a Git submodule.

```
git rm submodule
```

## Module Already Exists in Index.

in file .gitmodules - delete links to submodule (whole section with submodule name)

in file .git\\config - delete links to submodule, as in previous step

in folder .git\\modules - delete folder with relative path similar to relative path of "problem" module

## References

https://www.vogella.com/tutorials/GitSubmodules/article.html

https://stackoverflow.com/questions/12218420/add-a-submodule-which-cant-be-removed-from-the-index/39189599
