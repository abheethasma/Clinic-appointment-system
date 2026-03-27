from data_service import PatientMockDataService


class PatientService:
    def __init__(self):
        self.data_service = PatientMockDataService()

    def get_all(self):
        return self.data_service.get_all_patients()

    def get_by_id(self, patient_id: int):
        return self.data_service.get_patient_by_id(patient_id)

    def create(self, patient_data):
        return self.data_service.add_patient(patient_data)

    def update(self, patient_id: int, patient_data):
        return self.data_service.update_patient(patient_id, patient_data)

    def delete(self, patient_id: int):
        return self.data_service.delete_patient(patient_id)