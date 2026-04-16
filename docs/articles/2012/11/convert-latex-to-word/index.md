---
title: Convert LaTeX to Word
created: 2012-11-13 00:02:08
date: 2026-04-15 19:27:00.303408
authors:
  - bendu
label: convert-latex-to-word
license: CC-BY-4.0
tags:
  - HTML
  - LaTeX
  - office
  - software
  - Word
---

`pandoc` is a general purpose tool for converting between different type of documents,
however,
it is not good at converting LaTeX code to word.
`tex4ht` is a better tool for converting LaTeX code to word.
The following are instructions to use `tex4ht` to convert LaTeX to word.

1. Compile your LaTeX code.
   Make sure that there are no error messages.
   Do not remove the temporary files produced when compiling your LaTeX code,
   as they are required by the `tex4ht` command.

1. Convert your LaTeX code to html document using the following command.

   ```
    mk4ht mzlatex you_latex_doc.tex
   ```

1. Open the html document using office tools (Microsoft Word, LibreOffice Writer, AbiWord, etc).

1. Save a copy of the html document to the right format you want.
