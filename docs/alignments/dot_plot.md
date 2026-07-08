# Dot Plot Visualizer

## Problem Statement

Given two sequences $S_1$ and $S_2$, map and visualize character similarities in a 2D comparative matrix grid to identify repeats, insertions, deletions (indels), and reverse complement inversions.

## Overview

A Dot Plot is a graphical method for comparing two biological sequences. A dot is placed at coordinate $(i, j)$ in a grid if sequence character $S_1[i]$ matches $S_2[j]$. To reduce comparison noise in long sequences, a sliding window size $w$ and a match threshold $t$ can be specified.

---

## Sliding Window Formulation

Let:
- $S_1$ be a sequence of length $n$.
- $S_2$ be a sequence of length $m$.
- $w$ be the sliding window size.
- $t$ be the minimum match threshold ($1 \le t \le w$).

We define the indicator match function for offset $k$ starting at positions $i$ and $j$ as:
$$\delta(i, j, k) = \begin{cases} 
1 & \text{if } S_1[i+k] = S_2[j+k] \\
0 & \text{if } S_1[i+k] \neq S_2[j+k]
\end{cases}$$

A dot is plotted at matrix coordinate $(i, j)$ if and only if the cumulative window matches satisfy the threshold $t$:
$$\sum_{k=0}^{w-1} \delta(i, j, k) \ge t$$

---

## Algorithmic Complexity

- **Time Complexity**: $\mathcal{O}(n \cdot m \cdot w)$ where $n = |S_1|$, $m = |S_2|$, and $w$ is the sliding window size, since every possible starting index pair $(i, j)$ is evaluated across a window of size $w$.
- **Space Complexity**: $\mathcal{O}(n \cdot m)$ to represent the comparative visual grid elements.
