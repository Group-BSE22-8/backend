from datetime import datetime

from sqlalchemy import text as sa_text
from sqlalchemy.dialects.postgresql import UUID

from app.models import db
from app.models.model_mixin import ModelMixin


class Project(ModelMixin):
    __tablename__ = 'projects'
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Project %r>' % self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated
        }
