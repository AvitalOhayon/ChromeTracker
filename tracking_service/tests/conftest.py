import pytest
from tracking.app import create_app
from flask.testing import FlaskClient


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture
def client(app) -> FlaskClient:
    return app.test_client()
