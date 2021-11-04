from app import db

# creating one to many relationships
class Genre(db.Model):
    __table__name = "genre"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
