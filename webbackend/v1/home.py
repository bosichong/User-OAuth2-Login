# -*- coding: UTF-8 -*-
"""
@Author   : J.sky
@Mail     : bosichong@qq.com
@QQ交流群  : python交流学习群号:217840699
@file      :home.py
@time     :2022/10/19

"""

from datetime import datetime, timedelta
from typing import Union, List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from webbackend import crud, schemas
from webbackend.database import get_db
from webbackend.rbac_decorator import verify_token_wrapper
from webbackend.schemas import Token, TokenData
from webbackend.schemas import User
from webbackend.utils import verify_password, APP_TOKEN_CONFIG, oauth2_scheme

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
    responses={404: {"description": "Not found"}},  # 请求异常返回数据
)


def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """
    根据id返回丹铅用户
    :param user_id:
    :param db:
    :return:
    """
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


def authenticate_user(db: Session, username: str, password: str, ):
    """
    认证用户
    :param username:
    :param password:
    :param db:
    :return:
    """
    user = crud.get_user_by_username(db, username=username)  # 获取用户信息
    if not user:
        return False
    # 校验密码成功返回用户user
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    """
    生成token
    :param data:
    :param expires_delta:
    :return:
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    # 生成带有时间限制的token
    encoded_jwt = jwt.encode(to_encode, APP_TOKEN_CONFIG.SECRET_KEY, algorithm=APP_TOKEN_CONFIG.ALGORITHM)
    return encoded_jwt


# 返回当前用户
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    username = verify_token(token)
    if username:
        user = crud.get_user_by_username(db, username=username)
    else:
        raise credentials_exception
    if user is None:
        raise credentials_exception
    return user


# 判断用户是否处于锁定状态
def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def verify_token(token: str = Depends(oauth2_scheme)):
    """
    验证token
    :param token:
    :return:
    """
    try:  # 从token中解码出用户名，
        payload = jwt.decode(token, APP_TOKEN_CONFIG.SECRET_KEY, algorithms=[APP_TOKEN_CONFIG.ALGORITHM])
        username: str = payload.get("sub")  # 从 token中获取用户名
        if username is None:
            return False
        token_data = TokenData(username=username)
        return token_data.username  # 验证成功返回用户名
    except JWTError:
        return False


@router.post("/verify_token")
def api_verify_token(token: str, ):
    """
    验证token的接口
    :param token:
    :return:
    """
    return {"res": verify_token(token)}


@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # 获取用户,如果没有或密码错误并提示错误.
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=APP_TOKEN_CONFIG.ACCESS_TOKEN_EXPIRE_MINUTES)
    # 生成token
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me", response_model=User)
@verify_token_wrapper()
def read_users_me(current_user: User = Depends(get_current_active_user),token: str = Depends(oauth2_scheme)):
    return current_user


@router.get("/items/")
@verify_token_wrapper()
def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@router.get("/users/", response_model=List[schemas.User])
@verify_token_wrapper()
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
