# databaseのカラム登録

from sqlalchemy.orm import Session
from db import models

def create_user(db: Session, username ,count, speed):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=username , count=count, speed=speed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_userrank(db: Session, usernameid ,rank):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.UserRank(usernameid=usernameid ,rank=rank)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_hourtable(db: Session, starttime ,remain):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_hourtable = models.HourTable(starttime=starttime , remain=remain)
    db.add(db_hourtable)
    db.commit()
    db.refresh(db_hourtable)
    return db_hourtable