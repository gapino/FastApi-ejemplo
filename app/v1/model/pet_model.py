from datetime import datetime

import peewee

from app.v1.utils.db import db
from .user_model import User


class Pet(peewee.Model):
    nombre = peewee.CharField()
    created_at = peewee.DateTimeField(default=datetime.now)
    user = peewee.ForeignKeyField(User, backref="pets")

    class Meta:
        database = db