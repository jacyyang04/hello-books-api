from app import db
from app.models.author import Author
from flask import Blueprint, jsonify, make_response, request, abort
from models.book import Book

# Blueprint
author_bp = Blueprint("author_bp", __name__, url_prefix="/authors")


# Helper Functions
def get_author_by_id(author_id):
    return Author.query.get_or_404(author_id, description=f"Author ID must be an integer")


# Routes
@author_bp.route("", methods=["POST"])
def create_author():
    request_body = request.get_json()

    if "name" not in request_body:
        return make_response("Invalid Request", 404)

    new_author = Author(name=request_body['name'])
    
    db.session.add(new_author)
    db.session.commit() 
    return make_response(f"Your author, {new_author.name}, has been created", 201)


@author_bp.route("", methods=["GET"])
def read_all_books():
    name_query = request.args.get('name')

    if name_query:
        authors = Author.query.filter_by(name=name_query)
    else:
        authors = Author.query.all()
    
    author_response = []
    for author in authors:
        author_response.append(
            {
                "id": author.id,
                "name": author.title
            }
        )

    return jsonify(author_response)

@author_bp.route("/<author_id>/books", methods=["GET"])
def handle_authors_books(author_id):
    author = Author.query.get(id=author_id)
    if author is None:
        return make_response("Author not found", 404)

    books_response = []
    for book in author.books:
        books_response.append(
            {
            "id": book.id,
            "title": book.title,
            "description": book.description
            }
        )
    return jsonify(books_response)

@author_bp.route("/<author_id>/books", methods=["POST"])
def handle_authors_books(author_id):
    author = Author.query.get(id=author_id)
    if author is None:
        return make_response("Author not found", 404)

    if request.method == "POST":
        request_body = request.get_json()
        new_book = Book(
            title=request_body["title"],
            description=request_body["description"],
            author=author
            )
        db.session.add(new_book)
        db.session.commit()
        return make_response(f"Book {new_book.title} by {new_book.author.name} successfully created", 201)