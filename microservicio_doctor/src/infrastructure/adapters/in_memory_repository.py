from typing import List, Optional
from src.domain.doctor_model import Doctor, DoctorUpdate
from src.application.ports.doctor_repository import DoctorRepositoryPort

class InMemoryDoctorRepository(DoctorRepositoryPort):
    def __init__(self):
        self.db: List[Doctor] = []

    def create(self, doctor: Doctor) -> Doctor:
        self.db.append(doctor)
        return doctor

    def get_all(self) -> List[Doctor]:
        return self.db

    def get_by_id(self, doctor_id: int) -> Optional[Doctor]:
        return next((p for p in self.db if p.id == doctor_id), None)

    def update(self, doctor_id: int, doctor_data: DoctorUpdate) -> Optional[Doctor]:
        doctor = self.get_by_id(doctor_id)
        if doctor:
            if doctor_data.nombre:
                doctor.nombre = doctor_data.nombre
            if doctor_data.especialidad:
                doctor.especialidad = doctor_data.especialidad
            return doctor
        return None

    def delete(self, doctor_id: int) -> bool:
        doctor = self.get_by_id(doctor_id)
        if doctor:
            self.db.remove(doctor)
            return True
        return False