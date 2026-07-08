# Smith-Waterman Algorithm

## Problem

Given two sequences `seq1` and `seq2`, find the most similar subsequences (local alignment) hidden within them, optimized through a scoring function.

## Overview

The Smith-Waterman algorithm is a dynamic programming algorithm used for local sequence alignment.

Unlike global alignment, local alignment does not force the entire sequence to align from end to end. It zeroes out negative scoring paths, allowing the algorithm to find highly conserved regions or matching subsequences within massive, otherwise unrelated genomes.

---

## Algorithm

Let:

- `match` = reward for matching characters
- `mismatch` = penalty for differing characters
- `gap` = penalty for inserting a gap

Define:
`dp[i][j]`
as the optimal local alignment score ending at:
`seq1[i-1]` and `seq2[j-1]`

Transition:
if `seq1[i-1] == seq2[j-1]`:
`dp[i][j] = max(0, dp[i-1][j-1] + match, dp[i-1][j] + gap, dp[i][j-1] + gap)`

otherwise:
`dp[i][j] = max(0, dp[i-1][j-1] + mismatch, dp[i-1][j] + gap, dp[i][j-1] + gap)`

The optimal score is not fixed at the bottom right. It is the maximum value found anywhere in the entire grid:
`max(dp)`

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

## Implementation Notes

After matrix construction:

1. Locate the highest-scoring cell.
2. Begin traceback from that cell.
3. Stop when a cell with score 0 is reached.

This extracts the optimal local alignment.
