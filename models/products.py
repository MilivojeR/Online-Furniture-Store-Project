from sqlalchemy import Float, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from users import User
from orders import Order

from database import Base

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String,nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="products")
    orders: Mapped[list["Order"]] = relationship(secondary="order_products", back_populates="products")