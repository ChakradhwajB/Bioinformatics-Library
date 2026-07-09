# Bioinformatics Platform API Documentation

The Bioinformatics Platform API is built using **FastAPI** to expose genetic sequence analysis and alignment tools.

When the server is running, the interactive documentation is automatically generated and accessible at:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## Base URL
All endpoints are prefixed with:
```text
http://127.0.0.1:8000/api/v1
```

---

## 1. Alignments Router (`/alignments`)

### POST `/alignments/hamming-distance`
Calculates the Hamming Distance between two sequences of equal length (compares characters up to the length of the shorter sequence).

* **Request Body**:
  ```json
  {
    "seq1": "GGCCG",
    "seq2": "GGTCG"
  }
  ```
* **Response Body**:
  ```json
  {
    "status": "success",
    "distance": 1
  }
  ```

---

### POST `/alignments/levenshtein-distance`
Calculates the Levenshtein Distance (edit distance) between two sequences.

* **Request Body**:
  ```json
  {
    "seq1": "AGTACG",
    "seq2": "ATGACG"
  }
  ```
* **Response Body**:
  ```json
  {
    "status": "success",
    "distance": 1
  }
  ```

---

### POST `/alignments/align`
Performs either global or local sequence alignment depending on the `alignment_type` parameter.

* **Request Body**:
  ```json
  {
    "seq1": "ACGTACGT",
    "seq2": "ACGTCGT",
    "match": 1,
    "mismatch": -1,
    "gap": -1,
    "alignment_type": "global"
  }
  ```
* **Response Body**:
  ```json
  {
    "status": "success",
    "score": 6,
    "alignment_1": "ACGTACGT",
    "alignment_2": "ACGT-CGT"
  }
  ```

---

### POST `/alignments/needleman-wunsch`
Performs global sequence alignment using the Needleman-Wunsch algorithm.

* **Request Body**:
  ```json
  {
    "seq1": "ACGTACGT",
    "seq2": "ACGTCGT",
    "match": 1,
    "mismatch": -1,
    "gap": -1
  }
  ```
* **Response Body**:
  ```json
  {
    "status": "success",
    "score": 6,
    "alignment_1": "ACGTACGT",
    "alignment_2": "ACGT-CGT"
  }
  ```

---

### POST `/alignments/smith-waterman`
Performs local sequence alignment using the Smith-Waterman algorithm.

* **Request Body**:
  ```json
  {
    "seq1": "ACGTACGT",
    "seq2": "ACGTCGT",
    "match": 1,
    "mismatch": -1,
    "gap": -1
  }
  ```
* **Response Body**:
  ```json
  {
    "status": "success",
    "score": 6,
    "alignment_1": "ACGTACGT",
    "alignment_2": "ACGT-CGT"
  }
  ```

---

## 2. Genetics Router (`/genetics`)

### POST `/genetics/complement`
Returns the complementary DNA strand.

* **Request Body**:
  ```json
  {
    "sequence": "AAAACCCGGT"
  }
  ```
* **Response Body**:
  ```json
  {
    "status": "success",
    "complement": "TTTTGGGCCA"
  }
  ```

---

### POST `/genetics/reverse-complement`
Returns the reverse complement of a DNA strand (complement in the antiparallel 5' to 3' direction).

* **Request Body**:
  ```json
  {
    "sequence": "AAAACCCGGT"
  }
  ```
* **Response Body**:
  ```json
  {
    "status": "success",
    "reverse_complement": "ACCGGGTTTT"
  }
  ```

---

### POST `/genetics/transcribe`
Transcribes a DNA sequence into the corresponding RNA sequence (substitutes T with U).

* **Request Body**:
  ```json
  {
    "sequence": "GATTACA"
  }
  ```
* **Response Body**:
  ```json
  {
    "status": "success",
    "transcribed_sequence": "GAUUACA"
  }
  ```

---

### POST `/genetics/translate`
Translates an RNA sequence into a protein sequence, stopping at any stop codon (`UAA`, `UAG`, `UGA`).

* **Request Body**:
  ```json
  {
    "rna_sequence": "AUGGCCAUGGCGCCCUAG"
  }
  ```
* **Response Body**:
  ```json
  {
    "status": "success",
    "protein": "MAMAP"
  }
  ```

---

### POST `/genetics/find-motif`
Finds all starting locations of a given motif within a genetic sequence, supporting overlapping sequences and returning 1-based indexing.

* **Request Body**:
  ```json
  {
    "sequence": "GATATATGCATATACTT",
    "motif": "ATAT"
  }
  ```
* **Response Body**:
  ```json
  {
    "status": "success",
    "positions": [2, 4, 10]
  }
  ```

---

## 3. IO Router (`/io`)

### POST `/io/validate`
Validates if the provided list of sequence lines conforms to the FASTA sequence format (only IUPAC nucleotide characters `A`, `T`, `G`, `C`, `N` case-insensitively).

* **Request Body**:
  ```json
  {
    "data": [
      ">Seq1",
      "ATCGN",
      "GATC"
    ]
  }
  ```
* **Response Body**:
  ```json
  {
    "status": "success",
    "is_valid": true
  }
  ```

---

### POST `/io/parse-fasta-text`
Accepts a raw FASTA text block as a string, validates its nucleotide sequences, and returns the parsed header-sequence record list.

* **Request Body**:
  ```json
  {
    "fasta_text": ">Seq1\nATCG\nGATC\n>Seq2\nTATA"
  }
  ```
* **Response Body**:
  ```json
  {
    "status": "success",
    "data": [
      {
        "header": "Seq1",
        "sequence": "ATCGGATC",
        "length": 8
      },
      {
        "header": "Seq2",
        "sequence": "TATA",
        "length": 4
      }
    ]
  }
  ```

---

### POST `/io/parse-fasta`
Accepts a `.fasta` file via `multipart/form-data` upload, validates it, and parses it.

* **Content-Type**: `multipart/form-data`
* **Request Payload**:
  * `file`: (Binary FASTA File upload)
* **Response Body**:
  ```json
  {
    "status": "success",
    "data": [
      {
        "header": "Seq1",
        "sequence": "ATCGGATC",
        "length": 8
      }
    ]
  }
  ```

---

### POST `/io/write-fasta`
Writes a record dictionary (header mapped to sequence) to a JSON file on the local file system.

* **Request Body**:
  ```json
  {
    "record": {
      "Seq1": "ATCGGATC",
      "Seq2": "TATA"
    },
    "output_file": "C:/path/to/output.json"
  }
  ```
* **Response Body**:
  ```json
  {
    "status": "success",
    "message": "Successfully wrote records to C:/path/to/output.json"
  }
  ```
