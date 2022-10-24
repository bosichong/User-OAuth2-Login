# -*- coding: UTF-8 -*-
"""
@Author   : J.sky
@Mail     : bosichong@qq.com
@QQ交流群  : python交流学习群号:217840699
@file      :schemas.py
@time     :2022/10/19

"""
from typing import Union

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    username: str
    password: str
    email: str


class User(UserBase):
    id: int
    username: str
    is_active: bool

    class Config:
        orm_mode = True
