from app.models.book import Book

# get all books and return no records
def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# get one book by id
def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == {
        'id' : 1,
        'title' : 'Ocean Book',
        'description' : 'watr 4evr'
    }

    new_book = Book.query.get(1)
    assert new_book.id == 1
    assert new_book.title == "Ocean Book"
    assert new_book.description == 'watr 4evr'

## COME BACK AND FIX THIS BUG

# add one book to database
def test_add_one_book_and_confirm_book_in_database(client, add_one_book):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200

    new_book = Book.query.get(1)
    assert new_book.id == 1
    assert new_book.title == "Dirt Book"
    assert new_book.description == 'soil'

