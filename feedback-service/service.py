from data_service import FeedbackMockDataService


class FeedbackService:
    def __init__(self):
        self.data_service = FeedbackMockDataService()

    def get_all(self):
        return self.data_service.get_all_feedbacks()

    def get_by_id(self, feedback_id: int):
        return self.data_service.get_feedback_by_id(feedback_id)

    def create(self, feedback_data):
        return self.data_service.add_feedback(feedback_data)

    def update(self, feedback_id: int, feedback_data):
        return self.data_service.update_feedback(feedback_id, feedback_data)

    def delete(self, feedback_id: int):
        return self.data_service.delete_feedback(feedback_id)