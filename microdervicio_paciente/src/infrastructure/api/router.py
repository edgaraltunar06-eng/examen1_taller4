from fastapi import APIRouter, HTTPException, status
from src.domain.paciente_model import Paciente, PacienteUpdate
from src.application.services.paciente_service import PacienteService
from src.infrastructure.adapters.in_memory_repository import InMemoryPacienteRepository

router = APIRouter()

repo = InMemoryPacienteRepository()
service = PacienteService(repo)

@router.post("/pacientes/", status_code=status.HTTP_201_CREATED, response_model=Paciente)
def create_paciente(paciente: Paciente):
    existing = service.get_paciente(paciente.id)
    if existing:
        raise HTTPException(status_code=400, detail="Paciente ID already exists")
    return service.create_paciente(paciente)

@router.get("/pacientes/", response_model=list[Paciente])
def read_pacientes():
    return service.get_pacientes()

@router.get("/pacientes/{paciente_id}", response_model=Paciente)
def read_paciente(paciente_id: int):
    paciente = service.get_paciente(paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente not found")
    return paciente

@router.put("/pacientes/{paciente_id}", response_model=Paciente)
def update_paciente(paciente_id: int, paciente_data: PacienteUpdate):
    updated_paciente = service.update_paciente(paciente_id, paciente_data)
    if not updated_paciente:
        raise HTTPException(status_code=404, detail="Paciente not found")
    return updated_paciente

@router.delete("/pacientes/{paciente_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_paciente(paciente_id: int):
    success = service.delete_paciente(paciente_id)
    if not success:
        raise HTTPException(status_code=404, detail="Paciente not found")
    return None