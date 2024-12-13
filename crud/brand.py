

from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select

from exceptions import DbnotFoundException
from models.brand import Brand
from schemas.brand import BrandCreate, BrandUpdate

def get_brand(db: Session, brand_id: int) -> Brand:
    # Using query to fetch an brand by ID
    brand = db.query(Brand).filter(Brand.brand_id == brand_id).first()  # `get()` is deprecated
    if not brand:
        raise DbnotFoundException
    return brand

def create_brand(db: Session, brand_data: BrandCreate) -> Brand:
    # Using model_dump() to convert the Pydantic model to a dict and pass to Brand model

    new_brand = Brand(
        brand_name=brand_data.brand_name,
        brand_picture_url=brand_data.brand_picture_url,
        brand_description=brand_data.brand_description,
    
    )
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)

    return new_brand

def update_brand(db: Session, brand_id: int, brand_data: BrandUpdate) -> Brand:
    # Get the brand object to be updated
    brand_being_updated = get_brand(db, brand_id)
    
    # Using model_dump() to get only the fields that were updated
    update_data = brand_data.model_dump(exclude_unset=True)

    # Loop over the updated fields and update the brand object
    for key, value in update_data.items():
        setattr(brand_being_updated, key, value)

    db.commit()  # Commit the changes to the database
    db.refresh(brand_being_updated)  # Refresh to get the updated object with new values
    
    return brand_being_updated

def delete_brand(db: Session, brand_id: int) -> None:
    # Fetch the brand object to be deleted
    brand = get_brand(db, brand_id)
    
    db.delete(brand)
    db.commit()  # Commit the delete operation

def get_brands(db: Session)->  list[Brand]:
        
        brands = db.query(Brand).all()
        return brands