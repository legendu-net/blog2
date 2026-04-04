---
title: "Tips on Git-Filter-Repo"
created: 2023-05-13 17:19:37
date: 2023-05-13 17:32:32
authors:
  - bendu
label: tips-on-git-filter-repo
license: CC-BY-4.0
tags:
  - Computer Science
  - programming
  - Git
  - filter-repo
  - git-filter-repo
  - strip
  - blobs
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Installation on Ubuntu / Debian

wajig install git-filter-repo

## Example Usages

Note: git-filter-repo changes the history commits of a Git repository 
which is a dangerous operation.
Make sure you know what you are doing!

git filter-repo --strip-blobs-bigger-than 30M --force

## References

https://github.com/newren/git-filter-repo
