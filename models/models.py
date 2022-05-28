from imageUpload.database import db
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    pic = db.Column(db.String(100), nullable=False)
    

