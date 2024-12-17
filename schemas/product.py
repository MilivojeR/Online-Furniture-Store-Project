from pydantic import BaseModel, EmailStr
from typing import List, Optional

from schemas.images import ProductImageCreate


class ProductBase(BaseModel):
    product_name:str
    product_price: float
    product_picture_url:str
    product_description: str

    class Config:
        orm_mode = True  


class ProductCreate(ProductBase):
     images: List[ProductImageCreate] = []
     pass


class ProductUpdate(ProductBase):
    product_name:Optional[str] = None
    product_price: Optional[float] = None
    product_picture_url:Optional[str] = None
    product_description: Optional[str] = None
    product_first_name: Optional[str] = None
    product_last_name: Optional[str] = None
    product_email: Optional[EmailStr] = None
    product_password: Optional[str] = None  
    product_adress:Optional[str] = None
    product_all_order_details:Optional[str] = None
    product_total_points_acquired:Optional[int] = None

class Product(ProductBase):
    product_id: int  

    class Config:
        orm_mode = True  
