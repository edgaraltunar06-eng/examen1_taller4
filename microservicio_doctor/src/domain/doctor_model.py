from pydantic import BaseModel, EmailStr
from typing import Optional

class Doctor (BaseModel):
    id: int
    nombre: str
    especialidad: str

class DoctorUpdate(BaseModel):
    nombre: Optional[str] = None
    especialidad: Optional[str] = None