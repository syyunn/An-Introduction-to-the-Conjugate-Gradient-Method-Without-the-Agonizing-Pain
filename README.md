# An-Introduction-to-the-Conjugate-Gradient-Method-Without-the-Agonizing-Pain
Pythonic implementation of __["An Introduction to the Conjugate Gradient Method Without the Agonizing Pain (Shewchuk, 1994)"](http://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf)__

## What is Conjugate-Gradient(CG)-Method?
Iterative method for solving large systems of linear equations. CG is effective
for systems of the form Ax = b where x is an unknown vector, b is a known vector, and 
A is a known, square, symmetric, positive-definite (or positive-indefinite) matrix

## Table of Contents

1. [Some Recalls from Linear Algebra](#)
    1. [QR Factorization and Back-substitution (in case A is Dense, not required to use CG)](#)
2. [CG (in case A is Sparse)](#)

## Figures

### Figure 2
<p align="center">
  <img src="/figures/2.png">
</p>

