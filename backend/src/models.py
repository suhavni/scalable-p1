
from . import db  # db comes from app.py

class Paste(db.Model):
    __tablename__ = 'paste'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(125), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)