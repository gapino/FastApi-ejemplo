from app.v1.model.user_model import User
from app.v1.model.pet_model import Pet

from app.v1.utils.db import db, get_db

def create_tables():
    with db:
        get_db()
        db.create_tables([User, Pet])