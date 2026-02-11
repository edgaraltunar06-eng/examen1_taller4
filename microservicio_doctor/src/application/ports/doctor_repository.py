from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.doctor_model import Doctor, DoctorUpdate

class DoctorRepositoryPort(ABC):
    @abstractmethod
    def create(self, doctor: Doctor) -> Doctor:
        pass
    @abstractmethod
    def get_all(self) -> List[Doctor]:
        pass
    @abstractmethod
    def get_by_id(self, doctor_id: int) -> Optional[Doctor]:
        pass
    @abstractmethod
    def update(self, doctor_id: int, doctor_data: DoctorUpdate) -> Optional[Doctor]:
        pass
    @abstractmethod
    def delete(self, doctor_id: int) -> bool:
        pass