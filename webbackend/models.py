# -*- coding: UTF-8 -*-
"""
@Author   : J.sky
@Mail     : bosichong@qq.com
@QQ交流群  : python交流学习群号:217840699
@file      :models.py
@time     :2022/10/19

"""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from webbackend.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True,index=True)
    hashed_password = Column(String,)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
