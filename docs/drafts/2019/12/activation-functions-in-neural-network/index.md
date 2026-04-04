---
title: "Activation Functions in Neural Network"
created: 2019-12-17 14:20:03
date: 2020-01-17 14:20:03
authors:
  - bendu
label: activation-functions-in-neural-network
license: CC-BY-4.0
tags:
  - AI
  - data science
  - machine learning
  - activation function
  - ReLU
  - GELU
  - Switch
  - Sigmoid
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## GELU

GELU is the best activation function currently (at least in NLP).

$$ GELU(x) == x \Phi(x) $$,

where $\Phi(x)$ is the cumulative distribution function of the standard normal distribution.


## ReLU

## ELU

## Swish

$$ f(x) = x \dot \sigma(x) $$,
where $\sigma(x)$ is the 
[sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function).

## Sigmoid

## References

https://mp.weixin.qq.com/s/LEPalstOc15CX6fuqMRJ8Q
