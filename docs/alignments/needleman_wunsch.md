# Needleman-Wunsch Algorithm

## Problem Statement

Given two sequences $S_1$ and $S_2$ of lengths $n$ and $m$, find the optimal global alignment that maximizes a similarity score based on rewards for matches and penalties for mismatches and gaps.

## Overview

The Needleman-Wunsch algorithm is a fundamental dynamic programming method used for global sequence alignment. It attempts to align two sequences from end-to-end to highlight homologous regions.

---

## Recurrence Relation & Dynamic Programming Formulation

Let:
- $\text{match}$: Reward score for matching characters.
- $\text{mismatch}$: Penalty score for mismatching characters.
- $\text{gap}$: Penalty score for introducing a gap.

We define the DP matrix cell $E_{i,j}$ as the optimal global alignment score between prefix $S_1[0 \dots i-1]$ and prefix $S_2[0 \dots j-1]$.

### Base Cases
$$
E_{i, 0} = i \times \text{gap} \quad \forall \ 0 \le i \le n
$$
$$
E_{0, j} = j \times \text{gap} \quad \forall \ 0 \le j \le m
$$

### Transition Formula
For $1 \le i \le n$ and $1 \le j \le m$, the value is computed as:
$$
E_{i, j} = \max \begin{cases} 
E_{i-1, j-1} + S(S_1[i-1], S_2[j-1]) & \text{(Match / Mismatch)} \\
E_{i-1, j} + \text{gap} & \text{(Deletion from } S_1\text{)} \\
E_{i, j-1} + \text{gap} & \text{(Insertion into } S_1\text{)}
\end{cases}
$$

Where the similarity function $S(a, b)$ is:
$$
S(a, b) = \begin{cases} 
\text{match} & \text{if } a = b \\
\text{mismatch} & \text{if } a \neq b
\end{cases}
$$

The optimal alignment score is stored in:
$$
\text{Score} = E_{n, m}
$$

---

## Algorithmic Complexity

- **Time Complexity**: $\mathcal{O}(n \cdot m)$ since every cell in the $n \times m$ grid is computed in constant time $\mathcal{O}(1)$.
- **Space Complexity**: $\mathcal{O}(n \cdot m)$ to store the dynamic programming score matrix for traceback.

Where:
- $n = |S_1|$ (length of Sequence 1)
- $m = |S_2|$ (length of Sequence 2)

---

## Traceback Procedure

The traceback starts at the bottom-right cell $E_{n, m}$ and reconstructs the alignment path backwards towards $E_{0, 0}$:
- If the current cell $E_{i, j}$ came from the diagonal cell $E_{i-1, j-1}$, we align $S_1[i-1]$ with $S_2[j-1]$.
- If it came from the top cell $E_{i-1, j}$, we align $S_1[i-1]$ with a gap `-` in $S_2$.
- If it came from the left cell $E_{i, j-1}$, we align a gap `-` in $S_1$ with $S_2[j-1]$.
