import pytest


@pytest.fixture
def client():
    from web import app

    app.app.config['TESTING'] = True
    yield app.app.test_client()
