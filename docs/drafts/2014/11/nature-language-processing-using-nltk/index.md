---
title: Nature Language Processing Using NLTK
created: 2014-11-22 14:30:18
date: 2026-04-05 19:42:38.221717
authors:
- bendu
label: nature-language-processing-using-nltk
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

