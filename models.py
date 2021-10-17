"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
        db.app = app
        db.init_app(app)

class User(db.Model):
    """User class"""

    __tablename__ = "users"
    
    @property
    def represent(self):
        p = self
        return f"<Pet id={p.id} first name={p.first_name} last name={p.last_name} image_url={p.image_url}>"

    id = db.Column(db.Integer,
            primary_key=True,
            autoincrement=True)
    first_name = db.Column(db.Text,
            nullable=False,
            unique=False)
    last_name = db.Column(db.Text,
            nullable=True,
            unique=False)
    image_url = db.Column(db.Text,
            nullable=True,
            unique=False)

