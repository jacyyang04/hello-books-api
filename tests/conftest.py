# file to store all my fixtures; confiure test: conftest

import pytest
from app import create_app
from app import db
from app.models.book import Book

# app
@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()  # creates empty database
        yield app
    
    with app.app_context():
        db.drop_all()   # deletes data

# client
@pytest.fixture
def client(app):
    return app.test_client()

# data
@pytest.fixture
def two_saved_books(app):
    # Arrange
    ocean_book = Book(title="Ocean Book",
                        description="watr 4evr")
    mountain_book = Book(title="Mountain Book",
                        description="i luv 2 climb rocks")

    db.session.add_all([ocean_book, mountain_book])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()


@pytest.fixture
def add_one_book(app):
    dirt_book = Book(title="Dirt Book",
                    description="soil")
    
    db.session.add(dirt_book)
    db.session.commit()