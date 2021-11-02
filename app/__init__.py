from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    # connection string
    # postgresql+psycopg2://postgres:postgres@localhost:5432/DB_NAME

    #db config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if not test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else:
        app.config["TESTING"] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    #
    db.init_app(app)
    migrate.init_app(app, db)
    
    #import models
    from .models.book import Book
    from .models.author import Author

    #import routes
    from .routes.book_route import books_bp
    app.register_blueprint(books_bp)

    from .routes.author_route import author_bp
    app.register_blueprint(author_bp)

    return app

