import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class ShoppingCart(Base):
    __tablename__ = "Shopping_cart"

    shopping_cart_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    shopping_cart_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    shopping_cart_price: Mapped[float] = mapped_column(Float, nullable=False)
    shopping_cart_date: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    