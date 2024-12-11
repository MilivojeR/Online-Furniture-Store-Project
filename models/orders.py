import datetime
from sqlalchemy import Column, DateTime, Integer, String, Table, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from users import User
from products import Product

from database import Base

order_products = Table(
    "order_products",
    Base.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("order_id", ForeignKey("orders.id"), primary_key=True)
)

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_date: Mapped[datetime.datetime] = mapped_column(DateTime,insert_default=func.now )
    address: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="orders")

    products: Mapped[list[Product]] = relationship(secondary="order_products", back_populates="orders")