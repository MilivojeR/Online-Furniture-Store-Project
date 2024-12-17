from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class ProductImage(Base):
    __tablename__ = "product_iamges"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    image_url: Mapped[str] = mapped_column(String, nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("Product.product_id"), nullable=False)

    product: Mapped["Product"] = relationship(back_populates="images")