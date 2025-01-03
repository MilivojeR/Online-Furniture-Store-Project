from pydantic import BaseModel, EmailStr
from typing import Optional, List


class ProductBase(BaseModel):
    product_name:str
    product_price: float
    product_video_url:str
    product_picture_url:str
    product_description: str
    product_description: str
    product_category_id:int

    class Config:
        orm_mode = True  


class ProductCreate(ProductBase):
     pass


class ProductUpdate(ProductBase):
    product_name:Optional[str] = None
    product_price: Optional[float] = None
    product_video_url:Optional[str] = None
    product_picture_url:Optional[str] = None
    product_description: Optional[str] = None
    product_category_id:Optional[int] = None

    
class Product(ProductBase):
    product_id: int  

    class Config:
        orm_mode = True  



class ProductGalleryBase(BaseModel):
    image_url: str
    product_id: int

    class Config:
        orm_mode = True


class ProductGalleryCreate(ProductGalleryBase):
    pass


class ProductGalleryUpdate(ProductGalleryBase):
    image_url: Optional[str] = None



class ProductGallery(ProductGalleryBase):
    gallery_id: int
    

    class Config:
        orm_mode = True


class ProductWithGallery(Product):
    gallery: List[ProductGallery] = []

    class Config:
        orm_mode = True