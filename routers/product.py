import crud.product as products
from schemas.product import ProductCreate, ProductUpdate, ProductBase, Product
from schemas.images import ProductImageCreate  # Import image schema
from exceptions import DbnotFoundException
from database import db
from crud.token import check_admin_role
from typing import List  # For typing lists of images
from fastapi import APIRouter, HTTPException, Depends

router = APIRouter(prefix="/products", tags=["product"])

# GET SINGLE PRODUCT
@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int, db: db):
    try:
        return products.get_product(db, product_id)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found!")

# GET ALL PRODUCTS
@router.get("/", response_model=list[Product])
def get_products(db: db):
    try:
        return products.get_products(db)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Not any products found!")

@router.post("", response_model=Product, status_code=201)
def create_product(product: ProductCreate, db: db):
    """
    Handles product creation and image URLs.
    """
    
    created_product = products.create_product(db, product)
    db.commit()
    db.refresh(created_product)
    

    if product.images:  # List of image URLs
        for image in product.images:
            new_image = ProductImageCreate(image_url=image.image_url)
            products.add_product_image(db, new_image, created_product.product_id)
    db.commit()
    
    return created_product

# UPDATE PRODUCT
@router.put("/{product_id}", response_model=ProductUpdate)
def update_product(product_id: int, product: ProductUpdate, db: db):
    try:
        updated_product = products.update_product(db, product_id, product)
        db.commit()
        db.refresh(updated_product)
        return updated_product
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found!")

# DELETE PRODUCT
@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: db):
    try:
        products.delete_product(db, product_id)
        db.commit()
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found!")
