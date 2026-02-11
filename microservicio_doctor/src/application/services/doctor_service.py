from typing import List, Optional
from src.domain.doctor_model import Doctor, DoctorUpdate
from src.application.ports.doctor_repository import DoctorRepositoryPort

class DoctorService:
    def __init__(self, repository: DoctorRepositoryPort):
        self.repository = repository

    def create_doctor(self, doctor: Doctor) -> Doctor:
        return self.repository.create(doctor)

    def get_doctores(self) -> List[Doctor]:
        return self.repository.get_all()

    def get_doctor(self, doctor_id: int) -> Optional[Doctor]:
        return self.repository.get_by_id(doctor_id)

    def update_doctor(self, doctor_id: int, doctor_data: DoctorUpdate) -> Optional[Doctor]:
        return self.repository.update(doctor_id, doctor_data)

    def delete_doctor(self, doctor_id: int) -> bool:
        return self.repository.delete(doctor_id)