from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    facebookId = db.Column(db.String(32))
    facebookToken = db.Column(db.String(128))
    createDate = db.Column(db.DateTime)
    modifiedDate = db.Column(db.DateTime)

