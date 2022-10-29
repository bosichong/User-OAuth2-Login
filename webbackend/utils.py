# -*- coding: UTF-8 -*-
"""
@Author   : J.sky
@Mail     : bosichong@qq.com
@QQ交流群  : python交流学习群号:217840699
@file      :utils.py
@time     :2022/10/22

"""
from passlib.context import CryptContext
from pydantic import BaseSettings


from fastapi.security import OAuth2PasswordBearer
# 执行生成token的地址
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/token")


class AppTokenConfig(BaseSettings):
    """
    在终端通过以下命令生成一个新的密匙:
    openssl rand -hex 32
    加密密钥 这个很重要千万不能泄露了，而且一定自己生成并替换。
    """
    SECRET_KEY = "ededcbe81f2e015697780d536196c0baa6ea26021ad7070867e40b18a51ff8da"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 5  # token失效时间


# 创建一个token的配置项。
APP_TOKEN_CONFIG = AppTokenConfig()

# 密码散列 pwd_context.hash(password)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 校验密码
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# hash密码
def get_password_hash(password):
    return pwd_context.hash(password)
