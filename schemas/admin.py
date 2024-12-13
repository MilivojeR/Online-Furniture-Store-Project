from pydantic import BaseModel, EmailStr
from typing import Optional

# Base schema that will be inherited by other schemas
class AdminBase(BaseModel):
    admin_first_name: str
    admin_last_name: str
    admin_email: EmailStr
    admin_password: str  # You might want to hash the password in a real app

    class Config:
        orm_mode = True  # This tells Pydantic to treat the ORM object like a dictionary

# Schema used for creating a new admin (doesn't require admin_id)
class AdminCreate(AdminBase):
    class Config:
        orm_mode = True  # This tells Pydantic to treat the ORM object like a dictionary

# Schema used for updating an existing admin (all fields optional)
class AdminUpdate(AdminBase):
    admin_first_name: Optional[str] = None
    admin_last_name: Optional[str] = None
    admin_email: Optional[EmailStr] = None
    admin_password: Optional[str] = None  # Optional field, can be used for updating the password

# Response schema used for returning admin data (with admin_id)
class Admin(AdminBase):


    class Config:
        orm_mode = True  # Allows Pydantic to serialize SQLAlchemy models correctly
