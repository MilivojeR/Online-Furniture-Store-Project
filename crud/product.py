

from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from exceptions import DbnotFoundException
from models.product import Product,ProductGallery
from schemas.product import ProductCreate, ProductUpdate,ProductGalleryCreate,ProductWithGallery
from fastapi import HTTPException, status
from sqlalchemy.orm import joinedload

def get_product(db: Session, product_id: int) -> ProductWithGallery:

    product = db.query(Product).options(joinedload(Product.gallery)).filter(Product.product_id == product_id).first()
    if not product:
        raise DbnotFoundException
    return product

def get_products(db: Session)->  list[ProductWithGallery]:
        
        products = db.query(Product).options(joinedload(Product.gallery)).all()
        return products

def delete_product(db: Session, product_id: int) -> None:

    product = get_product(db, product_id)
    
    db.delete(product)
    db.commit() 

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
    for gallery_item in product_data.gallery:
        new_gallery = ProductGallery(
            image_url=gallery_item.image_url,
            product_id=new_product.product_id,  
        )
        db.add(new_gallery)
    db.commit()  
    db.refresh(new_product)

    return new_product

def update_product(db: Session, product_id: int, product_data: ProductUpdate) -> Product:

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
   
     if product_data.gallery is not None:
        db.query(ProductGallery).filter(ProductGallery.product_id == product_id).delete()
        for gallery_item in product_data.gallery:
            new_gallery = ProductGallery(
                image_url=gallery_item.image_url, 
                product_id=product_id
            )
            db.add(new_gallery)

     db.commit()
     db.refresh(new_product)
     return new_product