import pytest
from datetime import datetime
from tracking.visit_data import Visit


def test_create_visit():
    """
    Test creating a Visit object.
    """
    visit = Visit(user_id=123, url="https://example.com", duration=120)
    assert visit.user_id == 123
    assert visit.url == "https://example.com"
    assert visit.duration == 120
    assert isinstance(visit.visit_id, str)
    assert isinstance(visit.date_time, datetime)


def test_to_db():
    """
    Test converting a Visit object to a dictionary.
    """
    visit = Visit(user_id=123, url="https://example.com", duration=120)
    visit_dict = visit.to_db()

    assert visit_dict["user_id"] == 123
    assert visit_dict["url"] == "https://example.com"
    assert visit_dict["duration"] == 120
    assert isinstance(visit_dict["visit_id"], str)
    assert isinstance(visit_dict["date_time"], datetime)


def test_from_db():
    """
    Test creating a Visit object from a dictionary.
    """
    visit_dict = {
        "visit_id": "1234",
        "user_id": 123,
        "url": "https://example.com",
        "duration": 120,
        "date_time": datetime.now()
    }

    visit = Visit.from_db(visit_dict)

    assert visit.user_id == visit_dict["user_id"]
    assert visit.url == visit_dict["url"]
    assert visit.duration == visit_dict["duration"]
    assert visit.visit_id == visit_dict["visit_id"]
    assert visit.date_time == visit_dict["date_time"]

