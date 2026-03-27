from fastapi import FastAPI, HTTPException, status
from typing import List
from models import Feedback, FeedbackCreate, FeedbackUpdate
from service import FeedbackService

app = FastAPI(title="Feedback Microservice", version="1.0.0")

feedback_service = FeedbackService()


@app.get("/")
def read_root():
    return {"message": "Feedback Microservice is running"}


@app.get("/api/feedbacks", response_model=List[Feedback])
def get_all_feedbacks():
    return feedback_service.get_all()


@app.get("/api/feedbacks/{feedback_id}", response_model=Feedback)
def get_feedback(feedback_id: int):
    feedback = feedback_service.get_by_id(feedback_id)
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return feedback


@app.post("/api/feedbacks", response_model=Feedback, status_code=status.HTTP_201_CREATED)
def create_feedback(feedback: FeedbackCreate):
    return feedback_service.create(feedback)


@app.put("/api/feedbacks/{feedback_id}", response_model=Feedback)
def update_feedback(feedback_id: int, feedback: FeedbackUpdate):
    updated_feedback = feedback_service.update(feedback_id, feedback)
    if not updated_feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return updated_feedback


@app.delete("/api/feedbacks/{feedback_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_feedback(feedback_id: int):
    success = feedback_service.delete(feedback_id)
    if not success:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return None