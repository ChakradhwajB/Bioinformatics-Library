# Needleman-Wunsch Algorithm

## Problem

Given two sequences seq1 and seq2, find the longest common subsequence, with or without gaps, that is optimized through a scoring function.

## Overview

The Needleman-Wunsch algorithm is a dynamic programming algorithm used for
global sequence alignment.

Global alignment attempts to align two entire sequences from beginning to end,
maximizing a scoring function that rewards matches and penalizes mismatches
and gaps.

---

## Algorithm

Let:

- match = reward for matching characters
- mismatch = penalty for differing characters
- gap = penalty for inserting a gap

Define:

dp[i][j]

as the optimal alignment score between:

seq1[:i]
seq2[:j]

Transition:

if seq1[i-1] == seq2[j-1]:

dp[i][j] =
max(
dp[i-1][j-1] + match,
dp[i-1][j] + gap,
dp[i][j-1] + gap
)

otherwise:

dp[i][j] =
max(
dp[i-1][j-1] + mismatch,
dp[i-1][j] + gap,
dp[i][j-1] + gap
)

The optimal score is stored in:

dp[n][m]

---

## Complexity

Time Complexity:

O(nm)

Space Complexity:

O(nm)

where:

n = len(seq1)
m = len(seq2)

---

## Example

Input:

```python
score, a1, a2 = NeedlemanWunsch(
    "ACGTACGT",
    "ACGTCGT"
)
```

Output:

```text
Score: 6

ACGTACGT
|||| |||
ACGT-CGT
```

The algorithm inserts one gap to maximize similarity.

---

## Implementation Notes

This implementation performs:

1. Dynamic programming matrix construction
2. Traceback reconstruction
3. Alignment generation

Traceback begins at:

dp[n][m]

and continues until the origin:

dp[0][0]

---
