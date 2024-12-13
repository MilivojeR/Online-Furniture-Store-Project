
import datetime
from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Brand(Base):
    __tablename__ = "Brand"

    brand_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    brand_name: Mapped[str] = mapped_column(String(100), nullable=False)
    brand_picture_url: Mapped[str] = mapped_column(String(255), nullable=False)
    brand_description: Mapped[str] = mapped_column(Text, nullable=True)

