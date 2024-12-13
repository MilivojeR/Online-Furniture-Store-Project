

import crud.brand as brands 
from schemas.brand import  BrandCreate,BrandUpdate,BrandBase,Brand
from exceptions import DbnotFoundException
from database import db

from typing import Annotated
from fastapi import APIRouter, HTTPException, Query
router = APIRouter(prefix="/brand", tags=["brand"])



@router.get("/{brand_id}", response_model=Brand)
def get_brand(brand_id: int, db: db):
    try:
        return brands.get_brand(db, brand_id)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Brand {brand_id} not found!")


@router.get("/", response_model=list[Brand])
def get_brands( db: db):
    try:
        return brands.get_brands(db)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Not any procucts found!")


@router.post("", response_model=BrandCreate, status_code=201)
def create_brand(brand:BrandCreate, db: db):
    brand = brands.create_brand(db, brand)
    db.commit()
    db.refresh(brand)
    return brand


@router.put("/{brand_id}", response_model=BrandUpdate)
def update_brand(brand_id: int, brand: BrandUpdate, db: db):
    try:
        brand = brands.update_brand(db, brand_id, brand)
        db.commit()
        db.refresh(brand)
        return brand
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Brand {brand_id} not found!")


@router.delete("/{brand_id}", status_code=204)
def delete_brand(brand_id: int, db: db):
    try:
        brands.delete_brand(db, brand_id)
        db.commit()
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Brand {brand_id} not found!")

