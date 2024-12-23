from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey
from database import Base
from models.product import Product  # Assuming your Product model exists

class ShoppingCart(Base):
    __tablename__ = "shopping_carts"
    
    # Define the cart_id as a primary key
    cart_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    # Define the costumer_id with a ForeignKey relationship to the Costumer table
    costumer_id: Mapped[int] = mapped_column(Integer, ForeignKey("Costumer.costumer_id"), nullable=True)  # Nullable for guest users
    
    # Define the relationship with the Costumer model, with uselist=False for one-to-one relationship
    costumer: Mapped["Costumer"] = relationship("Costumer", back_populates="shopping_cart", uselist=False)
    
    # Define the relationship with CartItem, which links multiple items to the shopping cart
    items: Mapped[list["CartItem"]] = relationship("CartItem", back_populates="cart")
    

class CartItem(Base):
    __tablename__ = "cart_items"
    
    # Define cart_item_id as the primary key for CartItem
    cart_item_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    # Define the cart_id as a ForeignKey linking to ShoppingCart
    cart_id: Mapped[int] = mapped_column(Integer, ForeignKey("shopping_carts.cart_id"))
    
    # Define the product_id as a ForeignKey linking to the Product table
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("Product.product_id"))
    
    # Define quantity with a default value of 1
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    
    # Define the relationship with the ShoppingCart, back_populates indicates two-way relationship
    cart: Mapped["ShoppingCart"] = relationship("ShoppingCart", back_populates="items")
    
    # Define the relationship with the Product model
    product: Mapped["Product"] = relationship("Product", back_populates="cart_items")

