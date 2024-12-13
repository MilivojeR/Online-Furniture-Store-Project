import datetime
from sqlalchemy import DateTime, Float, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Revenue(Base):
    __tablename__ = "Revenue"

    revenue_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    revenue_amount: Mapped[float] = mapped_column(Float, nullable=False)
    revenue_information: Mapped[str] = mapped_column(String(255), nullable=False)

