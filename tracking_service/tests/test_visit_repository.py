import pytest
from tracking.visit_data import Visit
from tracking.repository.visit_repository import VisitRepository


repo = VisitRepository()


@pytest.fixture(scope='function')
def setup_repository():
    """
    Fixture to provide the repository for tests.
    """
    return repo


def test_create_visit(setup_repository):
    """
    Test adding a visit to the database.
    """
    repo = setup_repository
    visit = Visit(user_id="123", url="https://example.com", duration=120)
    visit_id = repo.create_visit(visit)
    assert visit_id is not None

    retrieved_visit = repo.get_visit_by_id(visit_id)
    assert retrieved_visit is not None
    assert retrieved_visit == visit
    assert retrieved_visit.to_db() == visit.to_db()


def test_get_visit_by_id(setup_repository):
    """
    Test retrieving a visit by its ID.
    """
    repo = setup_repository
    visit = Visit(user_id="123", url="https://example.com", duration=120)
    visit_id = repo.create_visit(visit)

    retrieved_visit = repo.get_visit_by_id(visit_id)
    assert retrieved_visit is not None
    assert retrieved_visit.to_db() == visit.to_db()


def test_get_all_visits(setup_repository):
    """
    Test retrieving all visits from the database.
    """
    repo = setup_repository
    visit1 = Visit(user_id="123", url="https://example.com/1", duration=120)
    visit2 = Visit(user_id="456", url="https://example.com/2", duration=150)
    repo.create_visit(visit1)
    repo.create_visit(visit2)

    all_visits = repo.get_all_visits()
    assert len(all_visits) >= 2  # Ensure at least the two visits are there
    assert any(vis.to_db() == visit1.to_db() for vis in all_visits)
    assert any(vis.to_db() == visit2.to_db() for vis in all_visits)


def test_update_visit(setup_repository):
    """
    Test updating a visit in the database.
    """
    repo = setup_repository
    visit = Visit(user_id="123", url="https://example.com", duration=120)
    visit_id = repo.create_visit(visit)

    update_fields = {"duration": 180}
    updated_count = repo.update_visit(visit_id, update_fields)
    assert updated_count == 1

    updated_visit = repo.get_visit_by_id(visit_id)
    assert updated_visit is not None
    updated_visit_dict = visit.to_db()
    updated_visit_dict.update(update_fields)
    assert updated_visit.to_db() == updated_visit_dict


def test_delete_visit(setup_repository):
    """
    Test deleting a visit from the database.
    """
    repo = setup_repository
    visit = Visit(user_id="123", url="https://example.com", duration=120)
    visit_id = repo.create_visit(visit)

    delete_count = repo.delete_visit(visit_id)
    assert delete_count == 1

    deleted_visit = repo.get_visit_by_id(visit_id)
    assert deleted_visit is None
