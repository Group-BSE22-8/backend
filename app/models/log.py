from app.models import db
from app.models.model_mixin import ModelMixin
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text


class Log(ModelMixin):
    __tablename__ = 'logs'

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    name = db.Column(db.String(256), nullable=False)

    def __init__(self, severity):
        self.severity = severity
        self.dateCreated = db.func.current_timestamp()


