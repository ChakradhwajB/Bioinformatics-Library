"""
Benchmark suite for the Bioinformatics core_lib.
Measures wall-clock runtime of every public function.
"""

import time
import random
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core_lib import (
    HammingDistance,
    LevenshteinDistance,
    NeedlemanWunsch,
    SmithWaterman,
    Complement,
    ReverseComplement,
    Transcribe,
    Translate,
    FindMotif,
    ValidateInput,
    FastaParse,
)

BASES = "ACGT"
RNA_BASES = "ACGU"

def random_dna(n):
    return "".join(random.choice(BASES) for _ in range(n))

def random_rna(n):
    return "".join(random.choice(RNA_BASES) for _ in range(n))

def make_fasta_lines(n):
    seq = random_dna(n)
    lines = [">BenchmarkSeq"]
    for i in range(0, len(seq), 80):
        lines.append(seq[i:i+80])
    return lines

def fmt(s):
    if s < 0.001:
        return f"{s*1_000_000:.1f}µs"
    elif s < 1.0:
        return f"{s*1_000:.3f}ms"
    else:
        return f"{s:.3f}s"

def bench(fn, *args):
    t0 = time.perf_counter()
    fn(*args)
    return time.perf_counter() - t0

# Sizes
LINEAR = [10, 100, 1_000, 10_000, 100_000]
QUAD = [10, 100, 500, 1_000, 2_000, 3_000, 4_000, 5_000]

BENCHMARKS = [
    ("HammingDistance",      "$\\mathcal{O}(\\min(n, m))$", LINEAR, lambda n: (random_dna(n), random_dna(n)),            HammingDistance),
    ("LevenshteinDistance",  "$\\mathcal{O}(n \\cdot m)$",  QUAD,   lambda n: (random_dna(n), random_dna(n)),            LevenshteinDistance),
    ("NeedlemanWunsch",      "$\\mathcal{O}(n \\cdot m)$",  QUAD,   lambda n: (random_dna(n), random_dna(n)),            NeedlemanWunsch),
    ("SmithWaterman",        "$\\mathcal{O}(n \\cdot m)$",  QUAD,   lambda n: (random_dna(n), random_dna(n)),            SmithWaterman),
    ("Complement",           "$\\mathcal{O}(n)$",           LINEAR, lambda n: (random_dna(n),),                          Complement),
    ("ReverseComplement",    "$\\mathcal{O}(n)$",           LINEAR, lambda n: (random_dna(n),),                          ReverseComplement),
    ("Transcribe",           "$\\mathcal{O}(n)$",           LINEAR, lambda n: (random_dna(n),),                          Transcribe),
    ("Translate",            "$\\mathcal{O}(n)$",           LINEAR, lambda n: (random_rna(n),),                          Translate),
    ("FindMotif",            "$\\mathcal{O}(n \\cdot m)$",  LINEAR, lambda n: (random_dna(n), random_dna(min(8, n))),    FindMotif),
    ("ValidateInput",        "$\\mathcal{O}(N)$",           LINEAR, lambda n: (make_fasta_lines(n),),                    ValidateInput),
    ("FastaParse",           "$\\mathcal{O}(N)$",           LINEAR, lambda n: (make_fasta_lines(n),),                    FastaParse),
]

def main():
    random.seed(42)
    all_results = {}

    for name, complexity, sizes, setup, fn in BENCHMARKS:
        print(f"\n  Benchmarking: {name}")
        results = []
        for n in sizes:
            args = setup(n)
            elapsed = bench(fn, *args)
            results.append((n, elapsed))
            print(f"    n={n:<8} -> {fmt(elapsed)}")
        all_results[name] = (complexity, results)

    out = os.path.join(os.path.dirname(__file__), "results.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write("# Benchmark Results\n\n")
        f.write(f"**Python version**: `{sys.version.split()[0]}`  \n")
        f.write(f"**Platform**: `{sys.platform}`  \n")
        f.write("**Method**: Single timed run per size using `time.perf_counter()`  \n\n")
        f.write("---\n\n")

        for name, (complexity, results) in all_results.items():
            f.write(f"## {name}\n\n")
            f.write(f"**Time Complexity**: {complexity}\n\n")
            f.write("| Sequence Length | Runtime |\n")
            f.write("|----------------|---------|\n")
            for size, elapsed in results:
                f.write(f"| {size:,} | {fmt(elapsed)} |\n")
            f.write("\n---\n\n")

    print(f"\n  Results written to: {out}")

if __name__ == "__main__":
    main()
