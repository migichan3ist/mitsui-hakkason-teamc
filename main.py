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

# ユーザー登録
@app.get("/users_create/{username}")
def user_create(username: str,db: Session = Depends(get_db)):
    count=1
    print(username)
    result = create.create_user(db=db, username=username,count=count)
    print("ユーザー登録完了")
    return result

# ユーザーのcount変更
@app.get("/register_point/{userId}/{userMoney}")
def user_create(userId: int, userMoney: int, db: Session = Depends(get_db)):
    # 現在の来場回数を取得
    print("ユーザーのcount変更")
    now_count = search.users_count(db=db, userId=userId)
    count = now_count + 1
    # 来場回数の更新
    update.users_count_update(db=db, userId=userId,count=count)
    # 更新後のユーザー情報取得
    result = search.users_check(db=db, userId=userId)
    print(result.count)
    print("ユーザー登録完了")
    return result