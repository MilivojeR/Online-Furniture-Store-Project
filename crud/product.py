

from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select

from exceptions import DbnotFoundException
from models.product import Product
from schemas.product import ProductCreate, ProductUpdate

def get_product(db: Session, product_id: int) -> Product:
    # Using query to fetch an product by ID
    product = db.query(Product).filter(Product.product_id == product_id).first()  # `get()` is deprecated
    if not product:
        raise DbnotFoundException
    return product

def create_product(db: Session, product_data: ProductCreate) -> Product:
    # Using model_dump() to convert the Pydantic model to a dict and pass to Product model

    new_product = Product(
        product_name=product_data.product_name,
        product_price=product_data.product_price,
        product_picture_url=product_data.product_picture_url,
        product_description=product_data.product_description,
    
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

def update_product(db: Session, product_id: int, product_data: ProductUpdate) -> Product:
    # Get the product object to be updated
    product_being_updated = get_product(db, product_id)
    
    # Using model_dump() to get only the fields that were updated
    update_data = product_data.model_dump(exclude_unset=True)

    # Loop over the updated fields and update the product object
    for key, value in update_data.items():
        setattr(product_being_updated, key, value)

    db.commit()  # Commit the changes to the database
    db.refresh(product_being_updated)  # Refresh to get the updated object with new values
    
    return product_being_updated

def delete_product(db: Session, product_id: int) -> None:
    # Fetch the product object to be deleted
    product = get_product(db, product_id)
    
    db.delete(product)
    db.commit()  # Commit the delete operation

def get_products(db: Session)->  list[Product]:
        
        products = db.query(Product).all()
        return products