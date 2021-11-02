from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request, abort

# Blueprint
author_bp = Blueprint("author_bp", __name__, url_prefix="/authors")


# Helper Functions



# Routes