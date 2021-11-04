from app import db
from sqlalchemy.orm import relationship

#an instance of sqlAlchemy; Book is a child class
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    genre = db.relationship('Genre', secondary="books_genre", backref="books")

#   author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
#   author = db.relationship("Author", back_populates="books")
    
    def to_dict(self):
        genres = []
        for genre in self.genre:
            genres.append(genre.name)

        if self.author:
            author = self.author.name
        else:
            author = None

        return {
                    "id": self.id,
                    "title": self.title,
                    "description": self.description,
                    "genre": genres,
                    "author": author
            }