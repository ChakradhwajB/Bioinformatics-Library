# FASTA Export

## Problem Statement

Export a key-value mapping of genetic sequences (such as parsed FASTA records) to a structured file.

## Overview

After parsing, analyzing, or modifying genetic sequences, it is helpful to save the results. This function serializes a dictionary of sequence records to a JSON file.

---

## Method

1. Open the target output file pathway in write (`"w"`) mode.
2. Serialize the dictionary to JSON format and write it to the file using an indentation level of 4.

---

## Complexity Analysis

- **Time Complexity**: $\mathcal{O}(N)$ where $N$ is the total length of the sequence records dictionary (keys + values) to serialize.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space during file write operations.
