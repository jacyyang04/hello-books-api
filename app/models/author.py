from app import db
from sqlalchemy.orm import relationship

# creating one to many relationships
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    book = db.relationship('book', backref='author')