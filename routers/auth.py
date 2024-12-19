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
    form_data: OAuth2PasswordRequestForm = Depends(),  # Accepts email and password
    db: Session = Depends(get_db)
):
    # Retrieve user by email from either Admin or Costumer table
    user = db.query(Admin).filter(Admin.admin_email == form_data.username).first() or \
           db.query(Costumer).filter(Costumer.costumer_email == form_data.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # Check password based on user type
    if isinstance(user, Admin):
        password_field = user.admin_password  # Access admin password
        user_email = user.admin_email  # Correct email field for Admin
    else:
        password_field = user.costumer_password  # Access costumer password
        user_email = user.costumer_email  # Correct email field for Costumer

    # Verify password
    if not verify_password(form_data.password, password_field):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # Determine the user's role
    role = "admin" if isinstance(user, Admin) else "costumer"
    
    # Create JWT token with correct email field
    access_token = create_access_token(data={"sub": user_email, "role": role})
    return {"access_token": access_token, "token_type": "bearer"}
