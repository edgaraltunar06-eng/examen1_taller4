from typing import List, Optional
from src.domain.paciente_model import Paciente, PacienteUpdate
from src.application.ports.paciente_repository import PacienteRepositoryPort

class PacienteService:
    def __init__(self, repository: PacienteRepositoryPort):
        self.repository = repository

    def create_paciente(self, paciente: Paciente) -> Paciente:
        return self.repository.create(paciente)

    def get_pacientes(self) -> List[Paciente]:
        return self.repository.get_all()

    def get_paciente(self, paciente_id: int) -> Optional[Paciente]:
        return self.repository.get_by_id(paciente_id)

    def update_paciente(self, paciente_id: int, paciente_data: PacienteUpdate) -> Optional[Paciente]:
        return self.repository.update(paciente_id, paciente_data)

    def delete_paciente(self, paciente_id: int) -> bool:
        return self.repository.delete(paciente_id)