from pydantic import BaseModel
from typing import List, Optional

# Schema for CartItem
class CartItemBase(BaseModel):
    product_id: int
    quantity: int

    class Config:
        orm_mode = True  # This allows Pydantic to work with ORM models

# Schema for ShoppingCart
class ShoppingCartBase(BaseModel):
    customer_id: Optional[int] = None  # Nullable for guest users
    items: List[CartItemBase]  # A list of CartItems in the shopping cart

    class Config:
        orm_mode = True  # This allows Pydantic to work with ORM models

# Schema for creating a shopping cart (could be used for POST request, for example)
class ShoppingCartCreate(ShoppingCartBase):
    pass  # No changes for creating, just inherits from the base

# Schema for returning the shopping cart (could be used for GET response)
class ShoppingCartResponse(ShoppingCartBase):
    shopping_cart_id: int  # The ID of the shopping cart

    class Config:
        orm_mode = True  # This allows Pydantic to work with ORM models
