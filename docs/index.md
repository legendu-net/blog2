---
site:
  hide_title_block: true
  hide_outline: true
---

# Blog

% This is a hack because hiding the title block removes the margin and title
% Whereas we just want to remove the button links etc.

<div style="margin-top: 1em;">

## Welcome to Chuanlong Ben Du's Blog! 👋

</div>

## Recent blog posts

:::{blog-posts}
:kind: table
:sort: date-desc
:path: {articles,drafts,outdated}/**/*.{md,ipynb}
:limit: 20
:::
