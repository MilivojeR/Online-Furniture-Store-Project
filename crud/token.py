from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from sqlalchemy.orm import Session

from schemas.token import TokenData

SECRET_KEY = "your-secret-key" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Create a JWT access token
def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Verify and decode JWT token
def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        if username is None or role is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token data",
            )
        return {"username": username, "role": role}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

# Dependency to get the current user from the token
def get_current_user(token: str = Depends(oauth2_scheme)) -> TokenData:
    payload = verify_token(token)
    return TokenData(username=payload["username"], role=payload["role"])

def get_current_user_role(token: str = Depends(oauth2_scheme)) -> str:
        payload = verify_token(token)
        return payload.get("role", "")


# Dependency to check if the user is an admin
def get_admin_user(token: str = Depends(oauth2_scheme)):
    role = get_current_user_role(token)
    if role != "Admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have access to this resource",
        )
    
def check_admin_role(token: str = Depends(oauth2_scheme)) -> None:
    payload = verify_token(token)
    role: Optional[str] = payload.get("role")
    if role != "Admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to access this resource",
        )

# Dependency to check if the user is a customer
def check_customer_role(token: str = Depends(oauth2_scheme)) -> None:
    payload = verify_token(token)
    role: Optional[str] = payload.get("role")
    if role != "Costumer":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to access this resource",
        )

def get_current_user_email(token: str = Depends(oauth2_scheme)) -> str:
    payload = verify_token(token)
    email: Optional[str] = payload.get("username")
    return email
 
