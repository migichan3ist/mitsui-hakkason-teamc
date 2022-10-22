# table更新

from sqlalchemy.orm import Session
from db import models

def users_count_update(db: Session,userId,count):
    query = db.query(models.User)
    count_update = query.filter(models.User.id == userId).first()
    print("更新")
    count_update.count = count
    print(count_update.count)
    db.commit()