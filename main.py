from contextlib import asynccontextmanager
from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt.exceptions import  InvalidTokenError
from pydantic import BaseModel
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from routers import admin,costumer,product,category,auth
from crud.token import get_current_user_role




@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting the app")
    Base.metadata.create_all(engine)
    yield
    print("Shutting down the app")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


app.include_router(admin.router)
app.include_router(auth.router)
app.include_router(costumer.router)
app.include_router(product.router)
app.include_router(category.router)


