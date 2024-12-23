

import crud.product as products 
from schemas.product import  ProductCreate,ProductUpdate,ProductBase,Product
from exceptions import DbnotFoundException
from database import db
from crud.token import check_admin_role

from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends




router = APIRouter()
@router.get("/product/{product_id}", response_model=Product, tags=["public"])
def get_product(product_id: int, db: db):
    try:
        return products.get_product(db, product_id)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found!")


@router.get("/product", response_model=list[Product], tags=["public"])
def get_products( db: db):
    try:
        return products.get_products(db)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Not any procucts found!")


@router.post("/product", response_model=ProductCreate, status_code=201,dependencies=[Depends(check_admin_role)], tags=["admin-only"])
def create_product(product:ProductCreate, db: db):
    product = products.create_product(db, product)
    db.commit()
    db.refresh(product)
    return product


@router.put("/product/{product_id}", response_model=ProductUpdate, dependencies=[Depends(check_admin_role)], tags=["admin-only"])
def update_product(product_id: int, product: ProductUpdate, db: db):
    try:
        product = products.update_product(db, product_id, product)
        db.commit()
        db.refresh(product)
        return product
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found!")


@router.delete("/product/{product_id}", status_code=204, dependencies=[Depends(check_admin_role)], tags=["admin-only"])
def delete_product(product_id: int, db: db):
    try:
        products.delete_product(db, product_id)
        db.commit()
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found!")

