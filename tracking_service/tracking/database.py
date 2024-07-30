from pymongo import MongoClient
from tracking.config import Config


class Database:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client['tracking_db']

    def get_collection(self, collection_name):
        return self.db[collection_name]


db = Database(Config.MONGO_URI)