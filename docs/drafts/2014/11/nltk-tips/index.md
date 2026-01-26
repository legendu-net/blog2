---
title: "Nature Language Processing Using NLTK"
date: 2014-11-22 14:30:18
modified: 2020-05-22 14:30:18
authors:
  - bendu
label: nltk-tips
license: CC-BY-4.0
tags:
  - machine learning
  - data mining
  - text mining
  - data science
  - NLP
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

nltk.util.ngrams
nltk.bigrams
nltk.PorterStemmer

    :::python
    from nltk.util import ngrams
    sentence = 'this is a foo bar sentences and i want to ngramize it'
    n = 6
    sixgrams = ngrams(sentence.split(), n)
    for grams in sixgrams:
        print grams

