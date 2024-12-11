from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from orders import Order
from products import Product

from database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Fname: Mapped[str] = mapped_column(String, nullable=False)
    Lname: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    products: Mapped[list["Product"]] = relationship(back_populates="user")
    orders: Mapped[list["Order"]] = relationship(back_populates="user")