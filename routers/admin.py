from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.token import check_admin_role,get_current_user_email
from schemas.admin import Admin, AdminCreate, AdminUpdate
from database import get_db
import crud.admin as admins
from exceptions import DbnotFoundException

router = APIRouter()

# Admin-only endpoint: Fetch a single admin by ID
@router.get("/admin/{admin_id}", response_model=Admin, dependencies=[Depends(check_admin_role)], tags=["admin-only"])
def get_admin(admin_id: int, db: Session = Depends(get_db)):
    try:
        return admins.get_admin_by_id(db, admin_id)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Admin {admin_id} not found!")

# Admin-only endpoint: Fetch all admins
@router.get("/admin/", response_model=list[Admin], dependencies=[Depends(check_admin_role)], tags=["admin-only"])
def get_admins(db: Session = Depends(get_db)):
    try:
        return admins.get_admins(db)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail="No admins found!")

# Admin-only endpoint: Create a new admin
@router.post("/admin/", response_model=AdminCreate, status_code=201, tags=["admin-only"])
def create_admin(admin: AdminCreate, db: Session = Depends(get_db)):
    admin = admins.create_admin(db, admin)
    return admin

# Admin-only endpoint: Update an admin's details
@router.put("/admin/{admin_id}", response_model=AdminUpdate, dependencies=[Depends(check_admin_role)], tags=["admin-only"])
def update_admin(admin_id: int, admin: AdminUpdate, db: Session = Depends(get_db)):
    try:
        admin = admins.update_admin(db, admin_id, admin)
        return admin
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Admin {admin_id} not found!")





@router.put("/admin-only/", response_model=AdminUpdate, dependencies=[Depends(check_admin_role)], tags=["admin-only"])
def update_current_admin( admin: AdminUpdate,admin_email: str = Depends(get_current_user_email),  db: Session = Depends(get_db)):
    
    try:
        admin = admins.update_current_admin(db, admin_email,admin)
        return admin
    except DbnotFoundException:
        raise HTTPException(status_code=401, detail=f"To upgrade login with new  credentials")
    












