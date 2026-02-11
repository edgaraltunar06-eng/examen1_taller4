from typing import List, Optional
from src.domain.paciente_model import Paciente, PacienteUpdate
from src.application.ports.paciente_repository import PacienteRepositoryPort

class InMemoryPacienteRepository(PacienteRepositoryPort):
    def __init__(self):
        self.db: List[Paciente] = []

    def create(self, paciente: Paciente) -> Paciente:
        self.db.append(paciente)
        return paciente

    def get_all(self) -> List[Paciente]:
        return self.db

    def get_by_id(self, paciente_id: int) -> Optional[Paciente]:
        return next((p for p in self.db if p.id == paciente_id), None)

    def update(self, paciente_id: int, paciente_data: PacienteUpdate) -> Optional[Paciente]:
        paciente = self.get_by_id(paciente_id)
        if paciente:
            if paciente_data.nombre:
                paciente.nombre = paciente_data.nombre
            if paciente_data.email:
                paciente.email = paciente_data.email
            return paciente
        return None

    def delete(self, paciente_id: int) -> bool:
        paciente = self.get_by_id(paciente_id)
        if paciente:
            self.db.remove(paciente)
            return True
        return False