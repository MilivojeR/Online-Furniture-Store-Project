

import crud.product as products 
from schemas.product import  ProductCreate,ProductUpdate,ProductBase,Product
from exceptions import DbnotFoundException
from database import db

from typing import Annotated
from fastapi import APIRouter, HTTPException, Query
router = APIRouter(prefix="/product", tags=["product"])



@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int, db: db):
    try:
        return products.get_product(db, product_id)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found!")


@router.get("/", response_model=list[Product])
def get_products( db: db):
    try:
        return products.get_products(db)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Not any procucts found!")


@router.post("", response_model=ProductCreate, status_code=201)
def create_product(product:ProductCreate, db: db):
    product = products.create_product(db, product)
    db.commit()
    db.refresh(product)
    return product


@router.put("/{product_id}", response_model=ProductUpdate)
def update_product(product_id: int, product: ProductUpdate, db: db):
    try:
        product = products.update_product(db, product_id, product)
        db.commit()
        db.refresh(product)
        return product
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found!")


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: db):
    try:
        products.delete_product(db, product_id)
        db.commit()
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found!")

