from pydantic import BaseModel, EmailStr
from typing import Optional


class CategoryBase(BaseModel):
    category_name:str
    category_picture_url:str
    category_description: str

    class Config:
        orm_mode = True  


class CategoryCreate(CategoryBase):
     pass


class CategoryUpdate(CategoryBase):
    category_name:Optional[str] = None
    category_picture_url:Optional[str] = None
    category_description: Optional[str] = None

class Category(CategoryBase):
    category_id: int  

    class Config:
        orm_mode = True  
