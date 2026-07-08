from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from core_lib import (
    HammingDistance,
    LevenshteinDistance,
    NeedlemanWunsch,
    SmithWaterman
)

router = APIRouter()

# --- Request/Response Models ---

class HammingRequest(BaseModel):
    seq1: str
    seq2: str

class HammingResponse(BaseModel):
    status: str
    distance: int

class LevenshteinRequest(BaseModel):
    seq1: str
    seq2: str

class LevenshteinResponse(BaseModel):
    status: str
    distance: int

class AlignmentRequest(BaseModel):
    seq1: str
    seq2: str
    match: int = 1
    mismatch: int = -1
    gap: int = -1
    alignment_type: str = "global"  # "global" or "local"

class AlignmentResponse(BaseModel):
    status: str
    score: int
    alignment_1: str
    alignment_2: str

class NeedlemanWunschRequest(BaseModel):
    seq1: str
    seq2: str
    match: int = 1
    mismatch: int = -1
    gap: int = -1

class SmithWatermanRequest(BaseModel):
    seq1: str
    seq2: str
    match: int = 1
    mismatch: int = -1
    gap: int = -1


# --- Endpoints ---

@router.post("/hamming-distance", response_model=HammingResponse)
def get_hamming_distance(request: HammingRequest):
    """Calculates the Hamming Distance between two genetic sequences."""
    try:
        distance = HammingDistance(request.seq1, request.seq2)
        return HammingResponse(status="success", distance=distance)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/levenshtein-distance", response_model=LevenshteinResponse)
def get_levenshtein_distance(request: LevenshteinRequest):
    """Calculates the Levenshtein Distance (edit distance) between two sequences."""
    try:
        distance = LevenshteinDistance(request.seq1, request.seq2)
        return LevenshteinResponse(status="success", distance=distance)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/align", response_model=AlignmentResponse)
def align_sequences(request: AlignmentRequest):
    """Performs global or local sequence alignment using Needleman-Wunsch or Smith-Waterman."""
    try:
        if request.alignment_type.lower() == "global":
            score, a1, a2 = NeedlemanWunsch(
                request.seq1, request.seq2, request.match, request.mismatch, request.gap
            )
        elif request.alignment_type.lower() == "local":
            score, a1, a2 = SmithWaterman(
                request.seq1, request.seq2, request.match, request.mismatch, request.gap
            )
        else:
            raise HTTPException(status_code=400, detail="alignment_type must be 'global' or 'local'")
        
        return AlignmentResponse(
            status="success", 
            score=score, 
            alignment_1=a1, 
            alignment_2=a2
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/needleman-wunsch", response_model=AlignmentResponse)
def align_needleman_wunsch(request: NeedlemanWunschRequest):
    """Performs global sequence alignment using the Needleman-Wunsch algorithm."""
    try:
        score, a1, a2 = NeedlemanWunsch(
            request.seq1, request.seq2, request.match, request.mismatch, request.gap
        )
        return AlignmentResponse(
            status="success", 
            score=score, 
            alignment_1=a1, 
            alignment_2=a2
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/smith-waterman", response_model=AlignmentResponse)
def align_smith_waterman(request: SmithWatermanRequest):
    """Performs local sequence alignment using the Smith-Waterman algorithm."""
    try:
        score, a1, a2 = SmithWaterman(
            request.seq1, request.seq2, request.match, request.mismatch, request.gap
        )
        return AlignmentResponse(
            status="success", 
            score=score, 
            alignment_1=a1, 
            alignment_2=a2
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
