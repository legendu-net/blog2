---
title: Save and Load PyTorch Models
created: 2020-04-09 13:30:28
date: 2026-04-13 23:15:23.290239
authors:
  - bendu
label: save-and-load-pytorch-models
license: CC-BY-4.0
tags:
  - computer science
  - deep learning
  - data science
  - machine learning
  - PyTorch
  - save
  - load
  - serialization
  - deserialization
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. PyTorch uses pickle to serialize and deserialize objects.

1. The PyTorch convention is
   to use the file extension `.pt` or `.pth` for saving model (or its parameters)
   and use the file extension `.tar` for saving checkpoints.

1. It is preferred to save model parameters rather than the whole model.

## References

[SAVING AND LOADING MODELS](https://pytorch.org/tutorials/beginner/saving_loading_models.html)

[SERIALIZATION SEMANTICS](https://pytorch.org/docs/master/notes/serialization.html)
