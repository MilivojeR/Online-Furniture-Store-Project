import datetime
from sqlalchemy import DateTime, Float, Integer, String, Text, func,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
from database import Base
from typing import List

class Product(Base):
    __tablename__ = "Product"
    product_name: Mapped[str] = mapped_column(Text, nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_price: Mapped[float] = mapped_column(Float, nullable=False)
    product_video_url: Mapped[str] = mapped_column(String(255), nullable=False)
    product_picture_url: Mapped[str] = mapped_column(String, nullable=False)
    product_description: Mapped[str] = mapped_column(Text, nullable=True)
    product_category_id: Mapped[int] = mapped_column(Integer, ForeignKey("Category.category_id"))
    
    # Relationship to category: Each product belongs to one category
    category: Mapped["Category"] = relationship("Category", back_populates="products")
    cart_items: Mapped[list["CartItem"]] = relationship("CartItem", back_populates="product")

    

