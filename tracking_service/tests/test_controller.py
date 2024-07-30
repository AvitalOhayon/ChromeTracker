# import pytest
# from flask.testing import FlaskClient
# from tracking.app import create_app
#
#
# # pytest tests/test_controller.py --disable-warnings -s
# @pytest.fixture
# def client() -> FlaskClient:
#     app = create_app()
#     app.config['TESTING'] = True
#     return app.test_client()
#
# def test_track_visit(client: FlaskClient):
#     response = client.post('/api/visits/track', json={
#         "user_id": "123",
#         "url": "https://example.com",
#         "duration": 120
#     })
#     assert response.status_code == 201
#     assert "visit_id" in response.get_json()
#
#
# def test_track_visit_missing_data(client: FlaskClient):
#     response = client.post('/api/visits/track', json={
#         "user_id": "123",
#         "url": "https://example.com"
#         # duration is missing
#     })
#     assert response.status_code == 400
#     assert response.get_json() == {"error": "Missing data"}
#
#
# def test_get_visits(client: FlaskClient):
#     response = client.get('/api/visits/visits/123')
#     assert response.status_code == 200
#     assert isinstance(response.get_json(), list)
#
#
# def test_update_visit(client: FlaskClient):
#     response = client.post('/api/visits/track', json={
#         "user_id": "123",
#         "url": "https://example.com",
#         "duration": 120
#     })
#     visit_id = response.get_json()["visit_id"]
#
#     update_response = client.put(f'/api/visits/{visit_id}', json={
#         "duration": 180
#     })
#     assert update_response.status_code == 200
#     assert update_response.get_json()["modified_count"] == 1
#
#     get_response = client.get(f'/visit/{visit_id}')
#     assert get_response.status_code == 200
#     updated_visit = get_response.get_json()
#     assert updated_visit["duration"] == 180
#
#
# def test_delete_visit(client: FlaskClient):
#     response = client.post('/api/visits/track', json={
#         "user_id": "123",
#         "url": "https://example.com",
#         "duration": 120
#     })
#     visit_id = response.get_json()["visit_id"]
#
#     delete_response = client.delete(f'/api/visits/{visit_id}')
#     assert delete_response.status_code == 200
#     assert delete_response.get_json()["deleted_count"] == 1
#
#     get_response = client.get(f'/visit/{visit_id}')
#     assert get_response.status_code == 404
#
#
# def test_get_visit(client: FlaskClient):
#     response = client.post('/api/visits/track', json={
#         "user_id": "123",
#         "url": "https://example.com",
#         "duration": 120
#     })
#     visit_id = response.get_json()["visit_id"]
#
#     get_response = client.get(f'/visit/{visit_id}')
#     assert get_response.status_code == 200
#     visit_data = get_response.get_json()
#     assert visit_data["visit_id"] == visit_id
#     assert visit_data["user_id"] == "123"
#     assert visit_data["url"] == "https://example.com"
#     assert visit_data["duration"] == 120
#
#
#


import pytest


import os
print("kkkkkkkkk")
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))

from flask.testing import FlaskClient
from tracking.app import create_app
from tracking.service.visit_service import VisitService


@pytest.fixture
def client() -> FlaskClient:
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def setup_data():
    visit_service = VisitService()
    visit_id = visit_service.create_visit("123", "https://example.com", 120)
    yield visit_id
    visit_service.delete_visit(visit_id)


def test_create_visit(client: FlaskClient):
    response = client.post('/api/visits/track', json={
        "user_id": "123",
        "url": "https://example.com",
        "duration": 120
    })
    assert response.status_code == 201
    data = response.get_json()
    assert "visit_id" in data


def test_create_visit_missing_data(client: FlaskClient):
    response = client.post('/api/visits/track', json={
        "user_id": "123",
        "url": "https://example.com"
        # duration is missing
    })
    assert response.status_code == 400
    data = response.get_json()
    assert data == {"error": "Missing data"}


def test_get_visits_by_user(client: FlaskClient):
    user_id = "123"
    response = client.get(f'/api/visits/{user_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)


def test_get_visit(client: FlaskClient, setup_data):
    visit_id = setup_data
    response = client.get(f'/api/visit/{visit_id}')
    if response.status_code == 200:
        data = response.get_json()
        assert "visit_id" in data
        assert "user_id" in data
        assert "url" in data
        assert "duration" in data
    else:
        assert response.status_code == 404
        data = response.get_json()
        assert data == {"error": "Visit not found"}
#
# def test_update_visit(client: FlaskClient, setup_data):
#     visit_id = setup_data
#     update_data = {"url": "https://new-url.com"}
#     response = client.put(f'/api/visits/{visit_id}', json=update_data)
#     assert response.status_code == 200
#     data = response.get_json()
#     assert "modified_count" in data
#
# def test_delete_visit(client: FlaskClient, setup_data):
#     visit_id = setup_data
#     response = client.delete(f'/api/visit/{visit_id}')
#     assert response.status_code == 200
#     data = response.get_json()
#     assert "deleted_count" in data

