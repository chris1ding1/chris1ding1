---
title: "JWT Authentication and Password Hashing in FastAPI"
slug: "jwt-authentication-and-password-hashing-in-fastapi"
keywords:
  - FastAPI
  - JWT
  - authentication
  - password hashing
  - PyJWT
  - pwdlib
  - Argon2
  - OAuth2
  - Python
  - access token
description: "Implement JWT authentication and secure password hashing in FastAPI using PyJWT and pwdlib with Argon2. Complete code examples for login, token generation, and user verification."
created: 2025-12-09 15:47:08
updated: 2025-12-09 16:20:09
---

## Install

### JWT

We need to install `PyJWT` to generate and verify the JWT tokens in Python.

```bash
uv add pyjwt
```

If you are planning to use digital signature algorithms like RSA or ECDSA, you should install the cryptography library dependency `pyjwt[crypto]`.

[PyJWT documentation](https://pyjwt.readthedocs.io/en/latest/index.html)

### Password hashing

Handle password hashes. It supports many secure hashing algorithms and utilities to work with them. 

The recommended algorithm is "Argon2".

```bash
uv add "pwdlib[argon2]"
```

[pwdlib documentation](https://frankie567.github.io/pwdlib/)

## Implementation

`app/routes/login.py`

```python
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.deps import SessionDep
from app.security import authenticate, create_access_token
from app.models import Token

router = APIRouter()


@router.post("/login/access-token")
def login_access_token(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = authenticate(
        session=session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    access_token = create_access_token(str(user.id))
    return Token(access_token=access_token)
```

`app/models.py`

```python
from sqlmodel import SQLModel

#...

class UserBase(SQLModel):
    #...

class UserPublic(UserBase):
    #...

# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"

# Contents of JWT token
class TokenPayload(SQLModel):
    sub: str | None = None
```

`app/security.py`

```python
from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash
from sqlmodel import Session, select

from app.config import settings
from app.models import User

password_hash = PasswordHash.recommended()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)

def authenticate(session: Session, email: str, password: str) -> User | None:
    statement = select(User).where(User.email == email)
    user = session.exec(statement).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(subject: str, expires_delta: timedelta | None = None) -> str:
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": subject}
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt
```

`app/deps.py`

```python
from collections.abc import Generator
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError
from sqlmodel import Session

from app.config import settings
from app.models import User, TokenPayload

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/login/access-token"
)


def get_db() -> Generator[Session, None, None]:
    #...


SessionDep = Annotated[Session, Depends(get_db)]
TokenDep = Annotated[str, Depends(reusable_oauth2)]


def get_current_user(session: SessionDep, token: TokenDep) -> User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (InvalidTokenError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = session.get(User, token_data.sub)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
```

`app/config.py`

```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # `openssl rand -hex 32`
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    # 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 11520


settings = Settings()
```

`app/routes/users.py`

```python
from typing import Any

from fastapi import APIRouter

from app.deps import CurrentUser
from app.models import UserPublic

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserPublic)
def read_user_me(current_user: CurrentUser) -> Any:
    """
    Get current user.
    """
    return current_user
```

## References
- [Full Stack FastAPI Template](https://github.com/tiangolo/full-stack-fastapi-template)
- [OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
