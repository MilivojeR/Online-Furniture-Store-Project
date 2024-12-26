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
    
  
    category: Mapped["Category"] = relationship("Category", back_populates="products")
    cart_items: Mapped[list["CartItem"]] = relationship("CartItem", back_populates="product")
    gallery: Mapped[list["ProductGallery"]] = relationship("ProductGallery", back_populates="product", cascade="all, delete-orphan")

    

class ProductGallery(Base):
    __tablename__ = "ProductGallery"
    gallery_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("Product.product_id"), nullable=False)
    image_url: Mapped[str] = mapped_column(String, nullable=False)
    
    product: Mapped["Product"] = relationship("Product", back_populates="gallery")