# フロントとバックのつなぎ

from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from db import models,create,search,update
from db.database import engine,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)
# DBセッションの作成
def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/aiueo")
async def root():
    return {"message": "aiueo"}

# ユーザー一覧
@app.get("/all_users_check")
def user_create(db: Session = Depends(get_db)):
    return search.all_users_check(db=db)

# idからユーザー検索
@app.get("/users_search_for_id/{userid}")
def users_check(userid : int,db: Session = Depends(get_db)):
    return search.users_check(db=db,userId=userid)

# ユーザー名からユーザー検索
@app.get("/users_search_for_name")
def all_users_check(db: Session = Depends(get_db)):
    return search.all_users_check(db=db)

# ユーザー登録
@app.get("/users_create/{username}")
def create_user(username: str,db: Session = Depends(get_db)):
    count = 1
    speed = 1
    print(username)
    result = create.create_user(db=db, username=username,count=count,speed=speed)
    print("ユーザー登録完了")
    return result
    
# ユーザーのcount変更
@app.get("/register_point/{userId}/{userMoney}")
def user_create(userId: int, userMoney: int, db: Session = Depends(get_db)):
    # 現在の来場回数を取得
    print("ユーザーのcount変更")
    now_count = search.users_count(db=db, userId=userId)
    increase_count = userMoney // 100
    count = now_count + increase_count
    # 来場回数の更新
    update.users_count_update(db=db, userId=userId,count=count)
    # 更新後のユーザー情報取得
    result = search.users_check(db=db, userId=userId)
    print(result.count)
    print("ユーザー登録完了")
    return result

# HourTable空なら作る
# 
@app.get("/hour_table")
def search_hourtable_table(db: Session = Depends(get_db)):
    if not search.hourtable_table(db=db):
        start_time = 11
        end_time = 23
        remain = 7
        for now_time in range(start_time,end_time):
            create.create_hourtable(db=db, starttime=now_time ,remain=remain)
    return search.hourtable_table(db=db)

@app.get("/catch_hour_table")
def search_hourtable_table(db: Session = Depends(get_db)):
    return search.hourtable_table(db=db)

# speedを増加させる
@app.get("/increase_speed/{userId}/{increaseSpeed}")
def increase_speed(userId: int, increaseSpeed: int, db: Session = Depends(get_db)):
    # 現在の来場回数を取得
    print("ユーザーのspeed変更")
    # now_speed = search.users_speed(db=db, userId=userId)
    speed = increaseSpeed
    # speedの更新
    update.users_speed_update(db=db, userId=userId,speed=speed)
     # 更新後のユーザー情報取得
    result = search.users_check(db=db, userId=userId)
    print(result.speed)
    print("ユーザー登録完了")
    return result

# speedを取得
@app.get("/search_speed/{userId}")
def increase_speed(userId: int, db: Session = Depends(get_db)):
    now_speed = search.users_speed(db=db, userId=userId)
    print("speeed取得")
    return now_speed

# ユーザーランキング
@app.get("/users_create_rank/{usernameid}/{rank}")
def create_user_rank(usernameid: int,rank: int,db: Session = Depends(get_db)):
    print(usernameid)
    result = create.create_userrank(db=db, usernameid=usernameid,rank=rank)
    print("ユーザー登録完了")
    return result

# rankを取得
@app.get("/search_user_rank/{userId}")
def search_user_rank(userId: int, db: Session = Depends(get_db)):
    now_speed = search.users_rank(db=db, userId=userId)
    print("speeed取得")
    return now_speed