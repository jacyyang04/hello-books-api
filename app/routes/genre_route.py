from app import db
from app.models.genre import Genre
from flask import Blueprint, jsonify, make_response, request, abort

# Blueprint
genre_bp = Blueprint("genre_bp", __name__, url_prefix="/genres")

# Helper Functions
def validate_genre(genre_id):
    return Genre.query.get_or_404(genre_id, description={"details": "invalid data"})

# Routes

