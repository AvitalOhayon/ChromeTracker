from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass
class Visit:
    """Class representing a visit to a website."""

    visit_id: str = None
    user_id: int = None
    url: str = None
    duration: int = None
    date_time: datetime = None

    def __post_init__(self):
        """ Initialize the Visit object."""
        if self.visit_id is None:
            self.visit_id = str(uuid.uuid4())
        if isinstance(self.date_time, str):
            self.date_time = datetime.fromisoformat(self.date_time)
        if self.date_time is None:
            self.date_time = datetime.now()

    def to_db(self):
        """ Convert the Visit object to a dictionary."""
        return {
            "visit_id": self.visit_id,
            "user_id": self.user_id,
            "url": self.url,
            "duration": self.duration,
            "date_time": self.date_time.isoformat()
        }

    @staticmethod
    def from_db(visit_db):
        """ Create a Visit object from a dictionary."""
        return Visit(
            visit_id=visit_db["visit_id"],
            user_id=visit_db["user_id"],
            url=visit_db["url"],
            duration=visit_db["duration"],
            date_time=visit_db["date_time"]
        )

