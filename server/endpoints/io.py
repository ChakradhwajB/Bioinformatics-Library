from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import Dict, List

from core_lib import (
    ValidateInput,
    FastaParse,
    FastaWrite
)

router = APIRouter()

# --- Request/Response Models ---

class ValidateRequest(BaseModel):
    data: List[str]

class ValidateResponse(BaseModel):
    status: str
    is_valid: bool

class FastaTextRequest(BaseModel):
    fasta_text: str

class FastaRecord(BaseModel):
    header: str
    sequence: str
    length: int

class ParseFastaResponse(BaseModel):
    status: str
    data: List[FastaRecord]

class FastaWriteRequest(BaseModel):
    record: Dict[str, str]
    output_file: str

class FastaWriteResponse(BaseModel):
    status: str
    message: str


# --- Endpoints ---

@router.post("/validate", response_model=ValidateResponse)
def validate_fasta_lines(request: ValidateRequest):
    """Validates if the provided list of lines conforms to FASTA sequence contents."""
    try:
        is_valid = ValidateInput(request.data)
        return ValidateResponse(status="success", is_valid=is_valid)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/parse-fasta-text", response_model=ParseFastaResponse)
def parse_fasta_text(request: FastaTextRequest):
    """Accepts a raw FASTA text string, parses it, and returns the sequence list."""
    lines = request.fasta_text.strip().split('\n')
    
    if not ValidateInput(lines):
        raise HTTPException(status_code=400, detail="Invalid FASTA format. Only A, C, G, T, N (case-insensitive) allowed in sequences.")
        
    parsed_records = FastaParse(lines)
    
    data_list = [
        FastaRecord(header=header, sequence=seq, length=len(seq))
        for header, seq in parsed_records.items()
    ]
    return ParseFastaResponse(status="success", data=data_list)


@router.post("/parse-fasta", response_model=ParseFastaResponse)
async def parse_fasta_file(file: UploadFile = File(...)):
    """Accepts an uploaded FASTA file, parses it, and returns the sequence list."""
    try:
        content = await file.read()
        text_data = content.decode("utf-8")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to read or decode file: {str(e)}")
        
    lines = text_data.strip().split('\n')
    
    if not ValidateInput(lines):
        raise HTTPException(status_code=400, detail="Invalid FASTA format. Only A, C, G, T, N (case-insensitive) allowed in sequences.")
        
    parsed_records = FastaParse(lines)
    
    data_list = [
        FastaRecord(header=header, sequence=seq, length=len(seq))
        for header, seq in parsed_records.items()
    ]
    return ParseFastaResponse(status="success", data=data_list)


@router.post("/write-fasta", response_model=FastaWriteResponse)
def write_fasta_records(request: FastaWriteRequest):
    """Writes a dictionary of genetic sequences to a JSON-formatted file on the server."""
    try:
        FastaWrite(request.record, request.output_file)
        return FastaWriteResponse(status="success", message=f"Successfully wrote records to {request.output_file}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to write file: {str(e)}")
