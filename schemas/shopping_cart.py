from pydantic import BaseModel
from typing import List, Optional


class CartItemBase(BaseModel):
    product_id: int
    quantity: int

    class Config:
        orm_mode = True  

class ShoppingCartBase(BaseModel):
    customer_id: Optional[int] = None  
    items: List[CartItemBase]  

    class Config:
        orm_mode = True  


class ShoppingCartCreate(ShoppingCartBase):
    pass  

class ShoppingCartResponse(ShoppingCartBase):
    shopping_cart_id: int 

    class Config:
        orm_mode = True  
