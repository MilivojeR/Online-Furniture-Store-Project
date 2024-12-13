
import crud.admin as admins 
from schemas.admin import  AdminCreate,AdminUpdate,AdminBase,Admin
from exceptions import DbnotFoundException
from database import db

from typing import Annotated
from fastapi import APIRouter, HTTPException, Query
router = APIRouter(prefix="/admin", tags=["admin"])



@router.get("/{admin_id}", response_model=Admin)
def get_admin(admin_id: int, db: db):
    try:
        return admins.get_admin(db, admin_id)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Admin {admin_id} not found!")


@router.post("", response_model=AdminCreate, status_code=201)
def create_admin(admin:AdminCreate, db: db):
    admin = admins.create_admin(db, admin)
    db.commit()
    db.refresh(admin)
    return admin


@router.put("/{admin_id}", response_model=AdminUpdate)
def update_admin(admin_id: int, admin: AdminUpdate, db: db):
    try:
        admin = admins.update_admin(db, admin_id, admin)
        db.commit()
        db.refresh(admin)
        return admin
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Admin {admin_id} not found!")


@router.delete("/{admin_id}", status_code=204)
def delete_admin(admin_id: int, db: db):
    try:
        admins.delete_admin(db, admin_id)
        db.commit()
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Admin {admin_id} not found!")






















