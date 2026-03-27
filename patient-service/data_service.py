from models import Patient


class PatientMockDataService:
    def __init__(self):
        self.patients = [
            Patient(
                id=1,
                name="John Perera",
                age=30,
                gender="Male",
                phone="0771234567",
                email="john.perera@example.com"
            ),
            Patient(
                id=2,
                name="Nisha Fernando",
                age=26,
                gender="Female",
                phone="0719876543",
                email="nisha.fernando@example.com"
            ),
            Patient(
                id=3,
                name="Kamal Silva",
                age=42,
                gender="Male",
                phone="0754443322",
                email="kamal.silva@example.com"
            ),
        ]
        self.next_id = 4

    def get_all_patients(self):
        return self.patients

    def get_patient_by_id(self, patient_id: int):
        return next((p for p in self.patients if p.id == patient_id), None)

    def add_patient(self, patient_data):
        new_patient = Patient(id=self.next_id, **patient_data.model_dump())
        self.patients.append(new_patient)
        self.next_id += 1
        return new_patient

    def update_patient(self, patient_id: int, patient_data):
        patient = self.get_patient_by_id(patient_id)
        if patient:
            update_data = patient_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(patient, key, value)
            return patient
        return None

    def delete_patient(self, patient_id: int):
        patient = self.get_patient_by_id(patient_id)
        if patient:
            self.patients.remove(patient)
            return True
        return False