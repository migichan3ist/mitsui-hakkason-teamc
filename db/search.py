# table検索

from sqlalchemy.orm import Session
from db import models

def all_users_check(db: Session):
    return db.query(models.User).all()

def users_check(db: Session,userId):
    return db.query(models.User).filter(models.User.id == userId).first()

def users_count(db: Session,userId):
    return db.query(models.User.count).filter(models.User.id == userId).first().count