# FASTA Parsing

## Problem Statement

Parse an iterable of FASTA-formatted lines (e.g., from a file or list of strings) into a key-value mapping of header labels to their concatenated genetic sequences.

## Overview

FASTA is a common text-based format where sequence descriptions are prefixed with `>` and the sequence itself spans one or more subsequent lines. The parser handles blank lines and concatenates multi-line sequences under their corresponding headers.

---

## Method

1. Initialize a dictionary `record`, a string `currHeader`, and a list `currSequence`.
2. Iterate through each line in the input:
   - Strip leading/trailing whitespace.
   - If the line is empty, skip it.
   - If the line starts with `>`:
     - If `currHeader` is already set, save the joined `currSequence` to `record[currHeader]`.
     - Update `currHeader` with the line contents after `>` (i.e., `line[1:]`), and reset `currSequence` to an empty list.
   - Otherwise, append the sequence line to `currSequence`.
3. After processing all lines, save the final sequence to `record[currHeader]` if `currHeader` is set.
4. Return the `record` dictionary.

---

## Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N)$ where $N$ is the total number of characters in the input sequence data.
- **Space Complexity**: $\mathcal{O}(N)$ to store the parsed records in memory.
