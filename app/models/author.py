from app import db

# creating one to many relationships
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    book = db.relationship('book', backref='author')
    # books = db.relationship("Book", back_populates="author")
