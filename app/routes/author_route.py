from app import db
from app.models.author import Author
from flask import Blueprint, jsonify, make_response, request, abort

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

