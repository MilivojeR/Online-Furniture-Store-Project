from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from crud.token import create_access_token, verify_password
from models.costumer import Costumer
from models.admin import Admin
from database import get_db
from schemas.token import Token

router = APIRouter()

@router.post("/auth/token", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),  
    db: Session = Depends(get_db)
):
    user = db.query(Admin).filter(Admin.admin_email == form_data.username).first()
    if user:
        password_field = user.admin_password  
        user_email = user.admin_email  
        role =user.admin_role  
    else:
        # If no Admin user is found, check if the user is a Costumer
        user = db.query(Costumer).filter(Costumer.costumer_email == form_data.username).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        password_field = user.costumer_password  # Access customer password
        user_email = user.costumer_email  # Correct email field for Costumer
        role = user.costumer_role # User role is "costumer"

    # Verify password
    if not verify_password(form_data.password, password_field):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    access_token = create_access_token(data={"sub": user_email, "role": role})
    return {"access_token": access_token, "token_type": "bearer"}
