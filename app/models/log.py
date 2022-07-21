from sqlalchemy import text as sa_text
from sqlalchemy.dialects.postgresql import UUID

from app.models import db
from app.models.model_mixin import ModelMixin


class Log(ModelMixin):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    # timestamp = db.Column(db.DateTime, index=True, default=db.func.current_timestamp())
    level = db.Column(db.String(8), index=True)
    message = db.Column(db.String(1024))
    # date_created = db.Column(db.DateTime, default=db.func.current_timestamp())


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
