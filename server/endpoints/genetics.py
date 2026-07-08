from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from core_lib import (
    Complement,
    ReverseComplement,
    Transcribe,
    Translate,
    FindMotif
)

router = APIRouter()

# --- Request/Response Models ---

class SequenceRequest(BaseModel):
    sequence: str

class ComplementResponse(BaseModel):
    status: str
    complement: str

class ReverseComplementResponse(BaseModel):
    status: str
    reverse_complement: str

class TranscribeResponse(BaseModel):
    status: str
    transcribed_sequence: str

class TranslateRequest(BaseModel):
    rna_sequence: str

class TranslateResponse(BaseModel):
    status: str
    protein: str

class FindMotifRequest(BaseModel):
    sequence: str
    motif: str

class FindMotifResponse(BaseModel):
    status: str
    positions: List[int]


# --- Endpoints ---

@router.post("/complement", response_model=ComplementResponse)
def get_complement(request: SequenceRequest):
    """Returns the complementary DNA strand."""
    try:
        res = Complement(request.sequence)
        return ComplementResponse(status="success", complement=res)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/reverse-complement", response_model=ReverseComplementResponse)
def get_reverse_complement(request: SequenceRequest):
    """Returns the reverse complement of a DNA strand."""
    try:
        res = ReverseComplement(request.sequence)
        return ReverseComplementResponse(status="success", reverse_complement=res)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/transcribe", response_model=TranscribeResponse)
def get_transcribe(request: SequenceRequest):
    """Returns the transcribed RNA sequence of a DNA strand."""
    try:
        res = Transcribe(request.sequence)
        return TranscribeResponse(status="success", transcribed_sequence=res)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/translate", response_model=TranslateResponse)
def translate_rna(request: TranslateRequest):
    """Translates an RNA sequence into a protein string."""
    try:
        protein = Translate(request.rna_sequence)
        return TranslateResponse(status="success", protein=protein)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/find-motif", response_model=FindMotifResponse)
def find_motif(request: FindMotifRequest):
    """Finds all starting locations of a given motif within a genetic sequence (1-based)."""
    try:
        positions = FindMotif(request.sequence, request.motif)
        return FindMotifResponse(status="success", positions=positions)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
