import datetime
from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column,relationship
from database import Base


class Category(Base):
    __tablename__ = "Category"

    category_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_name: Mapped[str] = mapped_column(String(100), nullable=False)
    category_picture_url: Mapped[str] = mapped_column(String(255), nullable=False)
    category_description: Mapped[str] = mapped_column(Text, nullable=True)
    
    products: Mapped[list["Product"]] = relationship(
        "Product", back_populates="category", cascade="all, delete-orphan")

