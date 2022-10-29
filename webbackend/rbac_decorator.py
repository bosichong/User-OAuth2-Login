from functools import wraps

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt

from webbackend.schemas import TokenData
from webbackend.utils import APP_TOKEN_CONFIG


def verify_token_wrapper():
    """定义一个token验证的装饰器"""

    def decorator(func):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="请先登陆后尝试",
            headers={"WWW-Authenticate": "Bearer"},
        )

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:  # 从token中解码出用户名，
                token = kwargs["token"]
                payload = jwt.decode(token, APP_TOKEN_CONFIG.SECRET_KEY, algorithms=[APP_TOKEN_CONFIG.ALGORITHM])
                username: str = payload.get("sub")  # 从 token中获取用户名
                print(username)
                if username is None:
                    return False
                token_data = TokenData(username=username)
                if token_data.username:
                    return func(*args, **kwargs)  # 要执行的函数
                else:
                    raise credentials_exception
            except JWTError:
                raise credentials_exception

        return wrapper

    return decorator



