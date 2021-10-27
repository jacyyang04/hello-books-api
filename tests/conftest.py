# file to store all my fixtures

import pytest
from app import create_app
from app import db

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()  # creates empty database
        yield app
    
    with app.app_context:
        db.drop_all()   # deletes data

# takes in app fixture, and acts as client
# will use our routes created
@pytest.fixture
def client(app):
    return app.test_client()
