
import datetime
from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Admin(Base):
    __tablename__ = "Admin"

    admin_id: Mapped[int] = mapped_column(Integer, autoincrement=True,primary_key=True)
    admin_first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    admin_last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    admin_password: Mapped[str] = mapped_column(String(128), nullable=False)
    admin_email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
