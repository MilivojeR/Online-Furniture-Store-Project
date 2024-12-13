from pydantic import BaseModel, EmailStr
from typing import Optional


class BrandBase(BaseModel):
    brand_name:str
    brand_picture_url:str
    brand_description: str

    class Config:
        orm_mode = True  


class BrandCreate(BrandBase):
     pass


class BrandUpdate(BrandBase):
    brand_name:Optional[str] = None
    brand_picture_url:Optional[str] = None
    brand_description: Optional[str] = None


class Brand(BrandBase):
    brand_id: int  

    class Config:
        orm_mode = True  
