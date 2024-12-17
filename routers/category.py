

import crud.category as categorys 
from schemas.category import  CategoryCreate,CategoryUpdate,CategoryBase,Category
from exceptions import DbnotFoundException
from database import db

from typing import Annotated
from fastapi import APIRouter, HTTPException, Query
router = APIRouter(prefix="/categorys", tags=["category"])



@router.get("/{category_id}", response_model=Category)
def get_category(category_id: int, db: db): # type: ignore
    try:
        return categorys.get_category(db, category_id)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found!")


@router.get("/", response_model=list[Category])
def get_categorys( db: db): # type: ignore
    try:
        return categorys.get_categorys(db)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Not any procucts found!")


@router.post("", response_model=CategoryCreate, status_code=201)
def create_category(category:CategoryCreate, db: db): # type: ignore
    category = categorys.create_category(db, category)
    db.commit()
    db.refresh(category)
    return category


@router.put("/{category_id}", response_model=CategoryUpdate)
def update_category(category_id: int, category: CategoryUpdate, db: db): # type: ignore
    try:
        category = categorys.update_category(db, category_id, category)
        db.commit()
        db.refresh(category)
        return category
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found!")


@router.delete("/{category_id}", status_code=204)
def delete_category(category_id: int, db: db): # type: ignore
    try:
        categorys.delete_category(db, category_id)
        db.commit()
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found!")

