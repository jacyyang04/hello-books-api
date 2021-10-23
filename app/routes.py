## This should have ran in terminal before this code can run.
# Make sure you run "export FLASK_ENV=development && flask run" to be in development mode
# run "export FLASK_ENV=development" before running "flask run"

from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST"])
def add_one_book():
    # get_json will give us body of the request
    request_body = request.get_json()
    new_book = Book(
        title=request_body['title'],
        description=request_body['description']
        )
    
    #adding to the db
    db.session.add(new_book) #like git, stagging changes
    db.session.commit() #committing to database

    #return response message to client
    return make_response(
        f"Your book, {new_book.title}, has been created", 201
    )


#######################################################################
#######################################################################

# hello_world_bp = Blueprint("hello_world_bp", __name__)

# class Book():
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Hocus Pocus", "A fantasy novel set in an imaginary world."),
#     Book(2, "Pikachutails", "A fantasy novel set in an imaginary world."),
#     Book(3, "Oogly Boogly Boo", "A fantasy novel set in an imaginary world.")
# ]

# @blueprint_name.route("/endpoint/path/here", methods=["GET"])
# @books_bp.route("", methods=["GET"])
# def get_all_books():
#     books_response = []

#     for book in books:
#         books_response.append( #vars(book)
#             {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }
#         )

#     return jsonify(books_response)

# @books_bp.route("/<book_id>", methods=["GET"])
# def get_one_book(book_id):
#     book_id = int(book_id)

#     for book in books:
#         if book.id == book_id:
#             return {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }


# using the blueprint decorator: 
# @blueprint_name.route("/endpoint/path/here", methods=["GET"])
# @hello_world_bp.route('/hello-world', methods=["GET"])
# def get_hello_world():
#     my_response = "Hello, World!"
#     return my_response

# @hello_world_bp.route('/hello/JSON', methods=["GET"])
# def hello_world_json():
#     return {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }, 201

# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"].append(new_hobby)
#     return response_body

