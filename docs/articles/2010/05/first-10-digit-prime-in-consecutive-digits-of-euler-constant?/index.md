---
title: First 10-digit Prime in Consecutive Digits of Euler Constant?
created: 2010-05-13 00:12:11
date: 2026-04-05 19:42:37.470912
authors:
- bendu
label: first-10-digit-prime-in-consecutive-digits-of-euler-constant?
license: CC-BY-4.0
tags:
- Mathematica
- Google
- Euler constant
- interview
- math
- fun problems
---
One day my friend Ru He asked me a question.

> What is the first 10-digit prime found in consecutive digits of e? 

This is an easy problem with the help of Mathematica.
The following is the Mathematica code I wrote to solve this question. 
It actually solves the general problem of first n-digit prime in consecutive digits of e.

    (*
    @param k: number of digits of the prime to be found in e*)
    @param n: number of digits of e to be used
    *)
    PrimeInE[k_: 10, n_: 10000] := Module[{app, temp, i, flag},
        app = N[E, n];
        flag = 0;
        For[i = 1, i <= n - k, i++,
        temp = app*10^(k - 1);
        temp = Floor[temp];
        flag++;
        If[PrimeQ[temp], Return[], app = (app - Floor[app]) 10]];
        Print["Please choose a bigger value for argument \"n\" in order to find the first ", k, "-digit prime in e."]
    ]

    PrimeInE[10]
    7427466391

    PrimeInE[30]
    182845904523536028747135266249
