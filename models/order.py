import datetime
from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Order(Base):
    __tablename__ = "Order"

    order_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    order_info: Mapped[str] = mapped_column(String(255), nullable=False)
    order_shipping_address: Mapped[str] = mapped_column(String(255), nullable=False)
    order_date: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
