# table検索

from sqlalchemy.orm import Session
from db import models

def all_users_check(db: Session):
    return db.query(models.User).all()

def users_check(db: Session,userId):
    return db.query(models.User).filter(models.User.id == userId).first()

def users_count(db: Session,userId):
    return db.query(models.User.count).filter(models.User.id == userId).first().count

# hourtableが空が田舎
def hourtable_table(db: Session):
    return db.query(models.HourTable).all()

# speed検索
def users_speed(db: Session,userId):
    return db.query(models.User.speed).filter(models.User.id == userId).first().speed

# speed検索
def users_rank(db: Session,userId):
    return db.query(models.UserRank).filter(models.User.id == userId).all()