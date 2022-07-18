from google.auth._helpers import utcnow
from sqlalchemy import text as sa_text
from sqlalchemy.dialects.postgresql import UUID

from app.models import db
from app.models.model_mixin import ModelMixin


class Log(ModelMixin):
    __tablename__ = 'logs'

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    timestamp = db.Column(db.DateTime, index=True, default=utcnow)
    level = db.Column(db.String(8), index=True)
    message = db.Column(db.String(1024))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('logs', lazy='dynamic'))

    def __repr__(self):
        return '<Log {}>'.format(self.message)

    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'level': self.level,
            'message': self.message,
            'user': self.user.to_dict()
        }
