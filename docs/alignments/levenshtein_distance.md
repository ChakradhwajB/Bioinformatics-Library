# Levenshtein Distance (Edit Distance)

## Problem Statement

Given two sequences $S_1$ and $S_2$, calculate the minimum number of single-character edit operations (insertions, deletions, or substitutions) required to transform $S_1$ into $S_2$.

## Overview

The Levenshtein distance measures the edit dissimilarity between two sequences. Unlike the Hamming distance, which only allows substitutions, Levenshtein distance handles alignments of different lengths by incorporating gap insertions ($\text{ins}$) and deletions ($\text{del}$).

---

## Recurrence Relation & Dynamic Programming Formulation

Let:
- $S_1$ be of length $n$
- $S_2$ be of length $m$

We define the DP cell $D_{i,j}$ as the minimum edit operations required to transform prefix $S_1[0 \dots i-1]$ into prefix $S_2[0 \dots j-1]$.

### Base Cases
Transforming a sequence to/from an empty sequence requires deleting/inserting all characters:
$$
D_{i, 0} = i \quad \forall \ 0 \le i \le n
$$
$$
D_{0, j} = j \quad \forall \ 0 \le j \le m
$$

### Transition Formula
For $1 \le i \le n$ and $1 \le j \le m$:
$$
D_{i, j} = \begin{cases} 
D_{i-1, j-1} & \text{if } S_1[i-1] = S_2[j-1] \quad \text{(No operation)} \\
\min \begin{cases} 
D_{i-1, j} + 1 & \text{(Deletion)} \\
D_{i, j-1} + 1 & \text{(Insertion)} \\
D_{i-1, j-1} + 1 & \text{(Substitution)}
\end{cases} & \text{otherwise}
\end{cases}
$$

The final minimum edit distance value is stored in:
$$
\text{Distance} = D_{n, m}
$$

---

## Algorithmic Complexity

- **Time Complexity**: $\mathcal{O}(n \cdot m)$ since every cell in the $n \times m$ grid is computed in constant time $\mathcal{O}(1)$.
- **Space Complexity**: $\mathcal{O}(n \cdot m)$ to store the dynamic programming distance matrix.

Where:
- $n = |S_1|$
- $m = |S_2|$
