from pydantic import BaseModel, EmailStr,Field
from typing import Optional


class AdminBase(BaseModel):
    admin_first_name: str
    admin_last_name: str
    admin_email: EmailStr
    

    class Config:
        orm_mode = True  


class AdminCreate(AdminBase):
     admin_role: str =Field(default="Admin") 
     admin_password: str



class AdminUpdate(AdminBase):
    admin_first_name: Optional[str] = None
    admin_last_name: Optional[str] = None
    admin_email: Optional[EmailStr] = None
    admin_password: Optional[str] = None  


class Admin(AdminBase):
    admin_id:int

    class Config:
        orm_mode = True  
