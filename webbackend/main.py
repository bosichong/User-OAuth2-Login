# -*- coding: UTF-8 -*-
"""
@Author   : J.sky
@Mail     : bosichong@qq.com
@QQ交流群  : python交流学习群号:217840699
@file      :home.py
@time     :2022/10/19

"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 解决跨域

from v1.home import router
from webbackend import models
from webbackend.database import engine

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

# 配置允许域名
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
    "http://localhost:3003",

]
# 配置允许域名列表、允许方法、请求头、cookie等
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 删除表，当更新表的结构时可以使用，但是会删除所有数据。慎用！！！！
# models.Base.metadata.drop_all(bind=engine)
# 在数据库中生成表结构
models.Base.metadata.create_all(bind=engine)

# app.include_router(demo.router)
app.include_router(router)


@app.get("/test/")
def test():
    return "hello world"


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)
