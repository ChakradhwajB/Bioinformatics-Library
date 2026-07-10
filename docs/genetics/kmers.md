# Overlapping K-mer Profiling

## Problem Statement

Given a genetic sequence $S$ and a k-mer length $k$, generate all overlapping substrings of length $k$, compute their frequency counts, and identify the most frequent k-mers.

## Overview

A **k-mer** is a substring of length $k$ contained within a biological sequence. Analyzing k-mer frequency distributions is a fundamental building block in computational biology, used in short-read assembly (De Bruijn graphs), metagenomics, and sequence alignment seeds.

---

## Mathematical Formulation

Let $S$ be a sequence of length $n$. The number of overlapping k-mers of length $k$ is:
```math
M = n - k + 1 \quad (\text{for } 1 \le k \le n)
```

The count of a specific k-mer $S_k$ within sequence $S$ is defined as:
```math
\text{Count}(S_k) = \sum_{i=0}^{n-k} [S[i \dots i+k-1] = S_k]
```
where $[P]$ is the Iverson bracket, returning $1$ if proposition $P$ is true, and $0$ otherwise.

The set of most frequent k-mers $F$ is defined as:
```math
F = \{S_k \mid \text{Count}(S_k) = \max_{X} \text{Count}(X)\}
```

---

## Complexity Analysis

- **Time Complexity**: $\mathcal{O}(n \cdot k)$ to extract and hash $n-k+1$ overlapping substrings of length $k$.
- **Space Complexity**: $\mathcal{O}(n \cdot k)$ to store the frequency dictionary containing at most $n-k+1$ unique k-mers.
