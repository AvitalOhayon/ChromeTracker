from bson import ObjectId
from tracking.database import db
from tracking.visit_data import Visit


class VisitRepository:
    """Class for interacting with the visits collection in MongoDB."""

    def __init__(self):
        """
        Initialize the VisitRepository instance.
        """
        self.collection = db.get_collection('visits')

    def create_visit(self, visit: Visit) -> str | None:
        """
        Save a visit to the database.

        :param visit: The visit object to save.
        :return: The saved visit id, None if an error occurred.
        """
        try:
            result = self.collection.insert_one(visit.to_db())
            return str(result.inserted_id)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_visit_by_id(self, visit_id: str) -> Visit | None:
        """
        Retrieve a visit from the database by its ID.

        :param visit_id: The ID of the visit to retrieve.
        :return: The retrieved visit object, None if not found.
        """
        try:
            print("kkkkkk", visit_id)
            data = self.collection.find_one({"_id": ObjectId(visit_id)})
            print("hhhhhhhhhhh", data)
            if data:
                return Visit.from_db(data)
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_all_visits(self) -> list[Visit]:
        """
        Retrieve all visits from the database.

        :return: A list of all visit objects in the collection.
        """
        try:
            return [Visit.from_db(data) for data in self.collection.find()]
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def update_visit(self, visit_id: str, update_fields: dict) -> int:
        """
        Update a visit in the database.

        :param visit_id: The ID of the visit to update.
        :param update_fields: A dictionary of fields to update.
        :return: The number of documents modified.
        """
        try:
            result = self.collection.update_one({"_id": ObjectId(visit_id)}, {"$set": update_fields})
            return result.modified_count
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0

    def delete_visit(self, visit_id: str) -> int:
        """
        Delete a visit from the database.

        :param visit_id: The ID of the visit to delete.
        :return: The number of documents deleted.
        """
        try:
            result = self.collection.delete_one({"_id": ObjectId(visit_id)})
            return result.deleted_count
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0
