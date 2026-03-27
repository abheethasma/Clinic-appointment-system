from pydantic import BaseModel
from typing import Optional


class Feedback(BaseModel):
    id: int
    appointment_id: int
    patient_id: int
    doctor_id: int
    rating: int
    comment: str


class FeedbackCreate(BaseModel):
    appointment_id: int
    patient_id: int
    doctor_id: int
    rating: int
    comment: str


class FeedbackUpdate(BaseModel):
    appointment_id: Optional[int] = None
    patient_id: Optional[int] = None
    doctor_id: Optional[int] = None
    rating: Optional[int] = None
    comment: Optional[str] = None