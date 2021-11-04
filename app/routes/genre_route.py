from app import db
from app.models.genre import Genre
from flask import Blueprint, jsonify, make_response, request, abort

# Blueprint
genre_bp = Blueprint("genre_bp", __name__, url_prefix="/genres")

# Helper Functions
def validate_genre(genre_id):
    return Genre.query.get_or_404(genre_id, description={"details": "invalid data"})

# Routes
@genre_bp.route("", methods=["GET"])
def read_all_genres():
    genres = Genre.query.all()
    genres_response = []
    for genre in genres:
        genres_response.append({
            "id": genre.id,
            "name": genre.name
            })
    return jsonify(genres_response)

@genre_bp.route("", methods=["POST"])
def add_genres():
    request_body = request.get_json()

    genre = Genre(name=request_body["name"])

    db.session.add(genre)
    db.session.commit()

    return jsonify(f"Genre {genre.name} was successfully created"), 201