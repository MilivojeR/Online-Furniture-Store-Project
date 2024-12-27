from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey
from database import Base
from models.product import Product  

class ShoppingCart(Base):
    __tablename__ = "shopping_carts"
    
    cart_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    costumer_id: Mapped[int] = mapped_column(Integer, ForeignKey("Costumer.costumer_id"), nullable=True)  
    costumer: Mapped["Costumer"] = relationship("Costumer", back_populates="shopping_cart", uselist=False)
    items: Mapped[list["CartItem"]] = relationship("CartItem", back_populates="cart")
    

class CartItem(Base):
    __tablename__ = "cart_items"

    cart_item_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    cart_id: Mapped[int] = mapped_column(Integer, ForeignKey("shopping_carts.cart_id"))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("Product.product_id"))
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    cart: Mapped["ShoppingCart"] = relationship("ShoppingCart", back_populates="items")
    product: Mapped["Product"] = relationship("Product", back_populates="cart_items")

