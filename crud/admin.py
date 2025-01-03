from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from exceptions import DbnotFoundException
from models.admin import Admin
from models.costumer import Costumer
from schemas.admin import AdminCreate, AdminUpdate

def get_admin_by_id(db: Session, admin_id: int) -> Admin:
    admin = db.query(Admin).filter(Admin.admin_id == admin_id).first()  
    if not admin:
        raise DbnotFoundException
    return admin


def get_admins(db: Session)->  list[Admin]:    
        admins = db.query(Admin).all()
        return admins

#Admin create with hasshed password.
def create_admin(db: Session, admin_data: AdminCreate) -> Admin:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_context.hash(admin_data.admin_password)
    costumer_with_email = db.query(Costumer).filter(Costumer.costumer_email == admin_data.admin_email).first()
    if costumer_with_email:
        raise HTTPException(
            status_code=400, 
            detail="Email address is already in use"
        )
    else:
        try:  
            new_admin = Admin(
                admin_first_name=admin_data.admin_first_name,
                admin_last_name=admin_data.admin_last_name,
                admin_email=admin_data.admin_email,
                admin_password=hashed_password,  
                admin_role=admin_data.admin_role
                )
            db.add(new_admin)
            db.commit()
            db.refresh(new_admin)
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(
                status_code=400, 
                detail="Email address is already in use."
        )  
    return new_admin


#admin update with hassed password
def update_admin(db: Session, admin_id: int, admin_data: AdminUpdate) ->Admin:
    update_data = admin_data.model_dump(exclude_unset=True)
    admin_being_updated = get_admin_by_id(db, admin_id)
    #hash password
    if "admin_password" in update_data:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        update_data["admin_password"] =pwd_context.hash(update_data["admin_password"])

    #check if there is a customer with same email because login expects email.
    admin_with_email = db.query(Admin).filter(Admin.admin_email == admin_data.admin_email).first()
    costumer_with_email = db.query(Costumer).filter(Costumer.costumer_email ==admin_data.admin_email).first()
    #if exists raise an error
    if admin_with_email or costumer_with_email:
            raise HTTPException(
                status_code=400, 
                detail="Email address is already in use"
            )

    else: 
        #if not do the update
        try:
            for key, value in update_data.items():
                setattr(admin_being_updated, key, value)
            db.commit()  
            db.refresh(admin_being_updated)   
        except IntegrityError as e:
            db.rollback()
      
            raise HTTPException(
                status_code=400, 
                detail="Email address is already in use."
        )  
    return admin_being_updated


#self update on addmin
def update_current_admin(db: Session, admin_email: str, admin_data: AdminUpdate) -> Admin:
 
    admin = db.query(Admin).filter(Admin.admin_email == admin_email).first()
    
    if not admin:
        raise DbnotFoundException("Admin not found, check the email and enter another one!")
    update_data = admin_data.model_dump(exclude_unset=True)
    if "admin_password" in update_data:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        update_data["admin_password"] = pwd_context.hash(admin_data.admin_password)

    
    admin_with_email = db.query(Admin).filter(Admin.admin_email == admin_data.admin_email).first()
    costumer_with_email = db.query(Costumer).filter(Costumer.costumer_email == admin_data.admin_email).first()

    if admin_with_email or costumer_with_email:
        raise HTTPException(
            status_code=400,
            detail="Email address is already in use"
        )

    try:
        for key, value in update_data.items():
            setattr(admin, key, value)

        db.commit()  
        db.refresh(admin)  
        
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="An error occurred while updating the admin."
        )  

    return admin
#admin delete
def delete_admin(db: Session, admin_id: int) -> None:
    admin = get_admin_by_id(db, admin_id)
    db.delete(admin)
    db.commit()
