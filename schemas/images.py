from pydantic import BaseModel

class ProductImageBase(BaseModel):
    image_url: str

class ProductImageCreate(ProductImageBase):
    image_url: str
    pass

class ProductImageResponse(ProductImageBase):
    id: int

    class Config:
        orm_mode=True