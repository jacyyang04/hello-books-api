
# get all books and return no records
def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# get one book by id
def test_get_on_book(client, two_saved_books):
    response = client.get("/books/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        'id' : 1,
        'title' : 'Ocean Book',
        'description' : 'watr 4evr'
    }

# add one book to database
def test_add_books(client, add_one_book):
    response = client.get("/books")
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        'title' : 'Dirt Book',
        'description' : 'soil'
    }