from tracking.repository.visit_repository import VisitRepository
from tracking.visit_data import Visit


class VisitService:
    def __init__(self):
        self.visit_repository = VisitRepository()

    def create_visit(self, user_id, url, duration) -> str | None:
        """"
        Create a new visit and save it to the database.

        :param user_id: The ID of the user making the visit.
        :param url: The URL visited by the user.
        :param duration: The duration of the visit in seconds.
        :return: The ID of the newly created visit.
        """
        visit = Visit(user_id=user_id, url=url, duration=duration)
        return self.visit_repository.create_visit(visit)

    def get_visits_by_user(self, user_id) -> list[Visit]:
        """
        Retrieve all visits for a specific user.
        :param user_id: The ID of the user.
        :return: List of visits made by the user.
        """
        visits = self.visit_repository.get_all_visits()
        return [visit for visit in visits if visit.user_id == user_id]

    def get_visit_by_id(self, visit_id) -> Visit | None:
        """
        Retrieve a visit by ID.
        :param visit_id:
        :return: visit object or None if not found.
        """
        return self.visit_repository.get_visit_by_id(visit_id)

    def delete_visit(self, visit_id) -> int:
        """
        Delete a visit by ID.
        :param visit_id:
        :return:
        """
        return self.visit_repository.delete_visit(visit_id)

    def update_visit(self, visit_id, update_fields) -> int:
        """
        Update a visit by ID.
        :param visit_id:
        :param update_fields:
        :return:
        """
        return self.visit_repository.update_visit(visit_id, update_fields)


