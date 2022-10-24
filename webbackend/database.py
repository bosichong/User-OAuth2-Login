# -*- coding: UTF-8 -*-
"""
@Author   : J.sky
@Mail     : bosichong@qq.com
@QQ交流群  : python交流学习群号:217840699
@file      :database.py
@time     :2022/10/19

"""
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 组装数据库的绝对地址
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, 'data.db')
# 数据库访问地址
SQLALCHEMY_DATABASE_URL = "sqlite:///" + DB_DIR

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
# 内存数据库
# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# 启动会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 数据模型的基类
Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
