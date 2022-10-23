# databasenのテーブルを作る

from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    count = Column(Integer())
    speed = Column(Integer())

class HourTable(Base):
    __tablename__ = 'hourtable'
    id = Column(Integer, primary_key=True, index=True)
    starttime = Column(Integer())
    remain = Column(Integer())

class UserRank(Base):
    __tablename__ = 'userranks'
    id = Column(Integer, primary_key=True, index=True)
    usernameid = Column(Integer)
    rank = Column(Integer())