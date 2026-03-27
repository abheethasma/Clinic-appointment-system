from models import Feedback


class FeedbackMockDataService:
    def __init__(self):
        self.feedbacks = [
            Feedback(
                id=1,
                appointment_id=1,
                patient_id=1,
                doctor_id=1,
                rating=5,
                comment="Very good consultation and clear explanation."
            ),
            Feedback(
                id=2,
                appointment_id=2,
                patient_id=2,
                doctor_id=2,
                rating=4,
                comment="Friendly doctor and smooth treatment."
            ),
            Feedback(
                id=3,
                appointment_id=3,
                patient_id=3,
                doctor_id=3,
                rating=5,
                comment="Doctor identified the issue quickly."
            ),
        ]
        self.next_id = 4

    def get_all_feedbacks(self):
        return self.feedbacks

    def get_feedback_by_id(self, feedback_id: int):
        return next((f for f in self.feedbacks if f.id == feedback_id), None)

    def add_feedback(self, feedback_data):
        new_feedback = Feedback(id=self.next_id, **feedback_data.model_dump())
        self.feedbacks.append(new_feedback)
        self.next_id += 1
        return new_feedback

    def update_feedback(self, feedback_id: int, feedback_data):
        feedback = self.get_feedback_by_id(feedback_id)
        if feedback:
            update_data = feedback_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(feedback, key, value)
            return feedback
        return None

    def delete_feedback(self, feedback_id: int):
        feedback = self.get_feedback_by_id(feedback_id)
        if feedback:
            self.feedbacks.remove(feedback)
            return True
        return False