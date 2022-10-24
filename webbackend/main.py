# -*- coding: UTF-8 -*-
"""
@Author   : J.sky
@Mail     : bosichong@qq.com
@QQ交流群  : python交流学习群号:217840699
@file      :home.py
@time     :2022/10/19

"""
from typing import List  # 用于定义对象数组

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from v1 import home
from webbackend import schemas, models, crud
from webbackend.database import engine
from webbackend.database import get_db

description = """
User-OAuth2-Login 是一个基于OAuth2的用户登陆验证系统. 🚀


## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="User-OAuth2-Login",
    description=description,
    version="0.0.1",
    terms_of_service="#",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

# 删除表，当更新表的结构时可以使用，但是会删除所有数据。慎用！！！！
# models.Base.metadata.drop_all(bind=engine)
# 在数据库中生成表结构
models.Base.metadata.create_all(bind=engine)

# app.include_router(demo.router)
app.include_router(home.router)


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/test/")
def test():
    return "hello world"


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)
