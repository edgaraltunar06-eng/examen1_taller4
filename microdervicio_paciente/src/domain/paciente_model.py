from pydantic import BaseModel, EmailStr
from typing import Optional
class Paciente (BaseModel):
    id: int
    nombre: str
    email: EmailStr

class PacienteUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None

class Doctor (BaseModel):
    id: int
    nombre: str
    especialidad: str

class DoctorUpdate(BaseModel):
    nombre: Optional[str] = None
    especialidad: Optional[str] = None