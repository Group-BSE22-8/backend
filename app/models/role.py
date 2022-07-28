from datetime import datetime, timedelta
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text
from sqlalchemy.orm import relationship, backref

from app.models import db
from app.models.model_mixin import ModelMixin


class Role(ModelMixin):
    """  Roles Table Definition """
    _tablename_ = 'roles'

    # fields of the Roles table
    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    name = db.Column(db.String(256), nullable=False)

    def __init__(self, name):
        """ initialize with name """
        self.name = name
