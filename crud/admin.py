

from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select

from exceptions import DbnotFoundException
from models.admin import Admin
from schemas.admin import AdminCreate, AdminUpdate

def get_admin(db: Session, admin_id: int) -> Admin:
    # Using query to fetch an admin by ID
    admin = db.query(Admin).filter(Admin.admin_id == admin_id).first()  # `get()` is deprecated
    if not admin:
        raise DbnotFoundException
    return admin

def create_admin(db: Session, admin_data: AdminCreate) -> Admin:
    # Using model_dump() to convert the Pydantic model to a dict and pass to Admin model
    new_admin = Admin(**admin_data.model_dump())

    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)

    return new_admin

def update_admin(db: Session, admin_id: int, admin_data: AdminUpdate) -> Admin:
    # Get the admin object to be updated
    admin_being_updated = get_admin(db, admin_id)
    
    # Using model_dump() to get only the fields that were updated
    update_data = admin_data.model_dump(exclude_unset=True)

    # Loop over the updated fields and update the admin object
    for key, value in update_data.items():
        setattr(admin_being_updated, key, value)

    db.commit()  # Commit the changes to the database
    db.refresh(admin_being_updated)  # Refresh to get the updated object with new values
    
    return admin_being_updated

def delete_admin(db: Session, admin_id: int) -> None:
    # Fetch the admin object to be deleted
    admin = get_admin(db, admin_id)
    
    db.delete(admin)
    db.commit()  # Commit the delete operation
