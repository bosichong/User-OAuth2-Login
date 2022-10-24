# -*- coding: UTF-8 -*-
"""
@Author   : J.sky
@Mail     : bosichong@qq.com
@QQ交流群  : python交流学习群号:217840699
@file      :home.py
@time     :2022/10/21

"""
import random

import pytest

from webbackend import crud
from webbackend.database import get_db
from webbackend.schemas import UserCreate


class TestCrud:
    def setup_class(self):
        print("hello qianzhi ")
        self.db = next(get_db())


    def test_get_user(self):
        user = crud.get_user(self.db, user_id=1)
        assert user

    def test_create_user(self):
        username = "hua" + str(random.randint(1, 999))
        email = "hua" + str(random.randint(1, 999)) + "@qq.com"
        password = "123456"
        user = UserCreate(username=username, password=password, email=email)
        new_user = crud.create_user(self.db, user=user)
        assert new_user


if __name__ == '__main__':
    pytest.main()
