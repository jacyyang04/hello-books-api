## This should have ran in terminal before this code can run.
# Make sure you run "export FLASK_ENV=development && flask run" to be in development mode
# run "export FLASK_ENV=development" before running "flask run"

from flask import Blueprint, jsonify

# connection string
# postgresql+psycopg2://postgres:postgres@localhost:5432/REPLACE_THIS_LAST_PART_WITH_DB_NAME


hello_world_bp = Blueprint("hello_world_bp", __name__)
books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

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

