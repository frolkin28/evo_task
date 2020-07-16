import uuid

from database import db


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    title = db.Column(db.String(255))
    ttl = db.Column(db.DateTime, nullable=False)

    def __init__(self, path, title, ttl):
        self.uuid = str(uuid.uuid4())
        self.title = title
        self.ttl = ttl
