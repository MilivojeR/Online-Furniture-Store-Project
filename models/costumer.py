import datetime
from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column,relationship
from database import Base
from models.shopping_cart import ShoppingCart

class Costumer(Base):
    __tablename__ = "Costumer"

    costumer_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    costumer_first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    costumer_last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    costumer_password: Mapped[str] = mapped_column(String(128), nullable=False)
    costumer_email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    costumer_all_order_details: Mapped[str] = mapped_column(Text, nullable=True)
    costumer_total_points_acquired: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    costumer_adress: Mapped[str] = mapped_column(String(255), nullable=False)
    costumer_role: Mapped[str] = mapped_column(String(50), default="Costumer", nullable=False) 

  
    costumer_day_created: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )  
    costumer_day_last_purchase: Mapped[datetime.datetime] = mapped_column(
        DateTime, nullable=True
    ) 
    shopping_cart: Mapped["ShoppingCart"] = relationship("ShoppingCart", back_populates="costumer", uselist=False)



