from fastapi import APIRouter, HTTPException, status
from src.domain.doctor_model import Doctor, DoctorUpdate
from src.application.services.doctor_service import DoctorService
from src.infrastructure.adapters.in_memory_repository import InMemoryDoctorRepository, InMemoryDoctorRepository

router = APIRouter()

repo = InMemoryDoctorRepository()
service = DoctorService(repo)

@router.post("/doctores/", status_code=status.HTTP_201_CREATED, response_model=Doctor)
def create_doctor(doctor: Doctor):
    existing = service.get_doctor(doctor.id)
    if existing:
        raise HTTPException(status_code=400, detail="Doctor ID already exists")
    return service.create_doctor(doctor)

@router.get("/doctores/", response_model=list[Doctor])
def read_doctores():
    return service.get_doctores()

@router.get("/doctores/{doctor_id}", response_model=Doctor)
def read_doctor(doctor_id: int):
    doctor = service.get_doctor(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@router.put("/doctores/{doctor_id}", response_model=Doctor)
def update_doctor(doctor_id: int, doctor_data: DoctorUpdate):
    updated_doctor = service.update_doctor(doctor_id, doctor_data)
    if not updated_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return updated_doctor

@router.delete("/doctores/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_doctor(doctor_id: int):
    success = service.delete_doctor(doctor_id)
    if not success:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return None