import datetime
from sqlalchemy import DateTime, Float, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Product(Base):
    __tablename__ = "Product"
    product_name: Mapped[str] = mapped_column(Text, nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_price: Mapped[float] = mapped_column(Float, nullable=False)
    product_picture_url: Mapped[str] = mapped_column(String(255), nullable=False)
    product_description: Mapped[str] = mapped_column(Text, nullable=True)
