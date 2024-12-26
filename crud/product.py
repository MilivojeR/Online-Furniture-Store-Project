

from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from exceptions import DbnotFoundException
from models.product import Product,ProductGallery
from schemas.product import ProductCreate, ProductUpdate,ProductGalleryCreate
from fastapi import HTTPException, status

def get_product(db: Session, product_id: int) -> Product:

    product = db.query(Product).filter(Product.product_id == product_id).first()  
    if not product:
        raise DbnotFoundException
    return product

def create_product(db: Session, product_data: ProductCreate) -> Product:


    new_product = Product(
        product_name=product_data.product_name,
        product_price=product_data.product_price,
        product_video_url=product_data.product_video_url,
        product_picture_url=product_data.product_picture_url,
        product_description=product_data.product_description,
        product_category_id=product_data.product_category_id,
    
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

def update_product(db: Session, product_id: int, product_data: ProductUpdate) -> Product:

    product_being_updated = get_product(db, product_id)
    update_data = product_data.model_dump(exclude_unset=True)

   
    for key, value in update_data.items():
        setattr(product_being_updated, key, value)

    db.commit()  
    db.refresh(product_being_updated)  
    
    return product_being_updated

def delete_product(db: Session, product_id: int) -> None:

    product = get_product(db, product_id)
    
    db.delete(product)
    db.commit() 

def get_products(db: Session)->  list[Product]:
        
        products = db.query(Product).all()
        return products

def get_products_by_category(db: Session, product_category_id: int) -> list[Product]:
    try:
       
        products = db.query(Product).filter(Product.product_category_id == product_category_id).all()
        return products
    except Exception as e:
        print(f"Error retrieving products by category: {e}")
        return []
    

def create_gallery(db: Session, gallery_data: ProductGalleryCreate) -> list[ProductGallery]:
    created_gallery_list = []
    
    # Split the image_urls string into a list using a semicolon as the delimiter
    image_urls = gallery_data.image_url.split(';')
    
    # Check if the product exists
    product = db.query(Product).filter(Product.product_id == gallery_data.product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {gallery_data.product_id} does not exist."
        )
    
    # Create gallery entries for each image URL
    for image_url in image_urls:
        new_gallery = ProductGallery(
            image_url=image_url.strip(),  # Remove any extra spaces around the URL
            product_id=gallery_data.product_id,
        )
        db.add(new_gallery)
        created_gallery_list.append(new_gallery)
    
    try:
        db.commit()  # Commit all gallery entries at once
        for gallery in created_gallery_list:
            db.refresh(gallery)  # Refresh to get the ID and other fields
        return created_gallery_list
    except Exception as e:
        db.rollback()  # Rollback the transaction if something goes wrong
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the galleries: {str(e)}"
        )
    

def delete_all_gallery_pictures(db: Session, product_id: int) -> None:
    # Retrieve all gallery pictures for the given product_id
    galleries_to_delete = db.query(ProductGallery).filter(ProductGallery.product_id == product_id).all()
    
    # Delete all retrieved gallery pictures
    for gallery in galleries_to_delete:
        db.delete(gallery)
    
    try:
        db.commit()  # Commit the changes (deletion)
    except Exception as e:
        db.rollback()  # Rollback in case of error
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while deleting gallery pictures: {str(e)}"
        )