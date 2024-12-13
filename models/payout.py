import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Payout(Base):
    __tablename__ = "Payout"

    payout_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    payout_method: Mapped[str] = mapped_column(String(50), nullable=False)
    payout_amount: Mapped[float] = mapped_column(Float, nullable=False)

 