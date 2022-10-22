# databaseのカラム登録

from sqlalchemy.orm import Session
from db import models

def create_user(db: Session, username ,count):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=username , count=count)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user