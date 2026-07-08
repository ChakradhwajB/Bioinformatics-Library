# Benchmark Results

**Python version**: `3.13.5`  
**Platform**: `win32`  
**Method**: Single timed run per size using `time.perf_counter()`  

---

## HammingDistance

**Time Complexity**: $\mathcal{O}(\min(n, m))$

| Sequence Length | Runtime |
|----------------|---------|
| 10 | 3.8µs |
| 100 | 6.2µs |
| 1,000 | 52.6µs |
| 10,000 | 633.2µs |
| 100,000 | 6.655ms |

---

## LevenshteinDistance

**Time Complexity**: $\mathcal{O}(n \cdot m)$

| Sequence Length | Runtime |
|----------------|---------|
| 10 | 132.2µs |
| 100 | 2.879ms |
| 500 | 89.657ms |
| 1,000 | 368.808ms |
| 2,000 | 1.357s |
| 3,000 | 3.101s |
| 4,000 | 13.386s |
| 5,000 | 15.564s |

---

## NeedlemanWunsch

**Time Complexity**: $\mathcal{O}(n \cdot m)$

| Sequence Length | Runtime |
|----------------|---------|
| 10 | 176.6µs |
| 100 | 7.832ms |
| 500 | 187.509ms |
| 1,000 | 610.183ms |
| 2,000 | 2.474s |
| 3,000 | 6.337s |
| 4,000 | 21.969s |
| 5,000 | 23.701s |

---

## SmithWaterman

**Time Complexity**: $\mathcal{O}(n \cdot m)$

| Sequence Length | Runtime |
|----------------|---------|
| 10 | 261.5µs |
| 100 | 15.150ms |
| 500 | 546.490ms |
| 1,000 | 1.598s |
| 2,000 | 4.037s |
| 3,000 | 12.308s |
| 4,000 | 13.940s |
| 5,000 | 24.482s |

---

## Complement

**Time Complexity**: $\mathcal{O}(n)$

| Sequence Length | Runtime |
|----------------|---------|
| 10 | 31.7µs |
| 100 | 7.1µs |
| 1,000 | 8.9µs |
| 10,000 | 30.5µs |
| 100,000 | 744.7µs |

---

## ReverseComplement

**Time Complexity**: $\mathcal{O}(n)$

| Sequence Length | Runtime |
|----------------|---------|
| 10 | 13.6µs |
| 100 | 11.1µs |
| 1,000 | 23.9µs |
| 10,000 | 108.7µs |
| 100,000 | 2.115ms |

---

## Transcribe

**Time Complexity**: $\mathcal{O}(n)$

| Sequence Length | Runtime |
|----------------|---------|
| 10 | 25.7µs |
| 100 | 13.7µs |
| 1,000 | 18.7µs |
| 10,000 | 66.0µs |
| 100,000 | 220.7µs |

---

## Translate

**Time Complexity**: $\mathcal{O}(n)$

| Sequence Length | Runtime |
|----------------|---------|
| 10 | 23.6µs |
| 100 | 7.7µs |
| 1,000 | 32.0µs |
| 10,000 | 68.7µs |
| 100,000 | 143.5µs |

---

## FindMotif

**Time Complexity**: $\mathcal{O}(n \cdot m)$

| Sequence Length | Runtime |
|----------------|---------|
| 10 | 4.1µs |
| 100 | 2.6µs |
| 1,000 | 11.7µs |
| 10,000 | 33.6µs |
| 100,000 | 3.291ms |

---

## ValidateInput

**Time Complexity**: $\mathcal{O}(N)$

| Sequence Length | Runtime |
|----------------|---------|
| 10 | 22.2µs |
| 100 | 8.9µs |
| 1,000 | 42.5µs |
| 10,000 | 401.8µs |
| 100,000 | 7.144ms |

---

## FastaParse

**Time Complexity**: $\mathcal{O}(N)$

| Sequence Length | Runtime |
|----------------|---------|
| 10 | 20.3µs |
| 100 | 8.6µs |
| 1,000 | 11.0µs |
| 10,000 | 56.2µs |
| 100,000 | 805.9µs |

---

