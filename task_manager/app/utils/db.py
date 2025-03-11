from pymongo import MongoClient
from flask import current_app


class MongoHelper:
    _instance = None  # Singleton instance placeholder

    def __new__(cls):
        """Ensure only one instance of MongoHelper is created."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = MongoClient(current_app.config['MONGO_URI'])
            print("MongoDB Connection Established")
        return cls._instance

    def get_database(self, db_name):
        """Get database instance."""
        return self.client[db_name]

    def close_connection(self):
        """Close MongoDB connection."""
        if self.client:
            self.client.close()
            print("MongoDB Connection Closed")
            MongoHelper._instance = None