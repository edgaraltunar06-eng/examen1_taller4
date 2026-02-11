from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.paciente_model import Paciente, PacienteUpdate

class PacienteRepositoryPort(ABC):
    @abstractmethod
    def create(self, paciente: Paciente) -> Paciente:
        pass
    @abstractmethod
    def get_all(self) -> List[Paciente]:
        pass
    @abstractmethod
    def get_by_id(self, paciente_id: int) -> Optional[Paciente]:
        pass
    @abstractmethod
    def update(self, paciente_id: int, paciente_data: PacienteUpdate) -> Optional[Paciente]:
        pass
    @abstractmethod
    def delete(self, paciente_id: int) -> bool:
        pass