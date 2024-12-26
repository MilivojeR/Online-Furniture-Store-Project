import crud.category as categorys
from schemas.category import CategoryCreate, CategoryUpdate, CategoryBase, Category
from crud.token import check_admin_role
from database import db
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from exceptions import DbnotFoundException

router = APIRouter(prefix="/category")


@router.get("/{category_id}", response_model=Category,tags=["public"])
def get_category(category_id: int, db: db,):
    try:
        return categorys.get_category(db, category_id)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found!")


@router.get("/", response_model=list[Category], tags=["public"])
def get_categorys(db: db):
    try:
        return categorys.get_categorys(db)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail="No categories found!")

@router.post("", response_model=CategoryCreate, status_code=201, dependencies=[Depends(check_admin_role)],tags=["admin-only"])
def create_category(category: CategoryCreate, db: db):
    category = categorys.create_category(db, category)
    db.commit()
    db.refresh(category)
    return category


@router.put("/{category_id}", response_model=CategoryUpdate, dependencies=[Depends(check_admin_role)],tags=["admin-only"])
def update_category(category_id: int, category: CategoryUpdate, db: db):
    try:
        category = categorys.update_category(db, category_id, category)
        db.commit()
        db.refresh(category)
        return category
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found!")


@router.delete("/{category_id}", status_code=204, dependencies=[Depends(check_admin_role)],tags=["admin-only"])
def delete_category(category_id: int, db: db):
    try:
        categorys.delete_category(db, category_id)
        db.commit()
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found!")

