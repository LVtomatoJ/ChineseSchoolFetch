from pydantic import BaseModel
from typing import Dict


class SchoolCodeInfo(BaseModel):
    school_id: str
    name: str


class SchoolCodeData(BaseModel):
    code: str
    message: str
    data: Dict[str, SchoolCodeInfo]
