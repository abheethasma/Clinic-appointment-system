from fastapi import FastAPI, HTTPException, status
from typing import List
from models import Patient, PatientCreate, PatientUpdate
from service import PatientService

app = FastAPI(title="Patient Microservice", version="1.0.0")

patient_service = PatientService()


@app.get("/")
def read_root():
    return {"message": "Patient Microservice is running"}


@app.get("/api/patients", response_model=List[Patient])
def get_all_patients():
    return patient_service.get_all()


@app.get("/api/patients/{patient_id}", response_model=Patient)
def get_patient(patient_id: int):
    patient = patient_service.get_by_id(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@app.post("/api/patients", response_model=Patient, status_code=status.HTTP_201_CREATED)
def create_patient(patient: PatientCreate):
    return patient_service.create(patient)


@app.put("/api/patients/{patient_id}", response_model=Patient)
def update_patient(patient_id: int, patient: PatientUpdate):
    updated_patient = patient_service.update(patient_id, patient)
    if not updated_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return updated_patient


@app.delete("/api/patients/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id: int):
    success = patient_service.delete(patient_id)
    if not success:
        raise HTTPException(status_code=404, detail="Patient not found")
    return None