import pytest
from pymongo.errors import ConnectionFailure
from tracking.database import db


def test_database_connection():
    """
    Test that the database connection is established successfully.
    """
    try:
        db.client.server_info()
    except ConnectionFailure:
        pytest.fail("Database connection failed")


def test_create_collection():
    """
    Test that a collection can be created successfully in the database.
    """
    collection_name = "test_collection"
    collection = db.get_collection(collection_name)

    # Insert a document to ensure the collection is created
    result = collection.insert_one({"test": "value"})
    assert result.acknowledged
    assert result.inserted_id is not None

    # Clean up by dropping the test collection
    db.db.drop_collection(collection_name)
