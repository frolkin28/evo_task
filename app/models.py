import uuid

from app.database import db


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    name = db.Column(db.String(120))
    path = db.Column(db.String(255))
    ttl = db.Column(db.DateTime, nullable=False)

    def __init__(self, path, name, ttl, file_uuid=None):
        if not file_uuid:
            self.uuid = str(uuid.uuid4())
        else:
            self.uuid = file_uuid
        self.path = path
        self.name = name
        self.ttl = ttl
