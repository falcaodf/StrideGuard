# app/schemas.py
from pydantic import BaseModel
from typing import List, Dict, Any

class STRIDEItem(BaseModel):
    id: str
    description: str
    evidence: List[str]
    likelihood: str
    impact: str
    remediation: List[str]

class STRIDEResult(BaseModel):
    stride: Dict[str, List[STRIDEItem]]  # keys: Spoofing, Tampering, ...
    raw: str = None
