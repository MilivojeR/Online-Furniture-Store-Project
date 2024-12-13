

from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select

from exceptions import DbnotFoundException
from models.category import Category
from schemas.category import CategoryCreate, CategoryUpdate

def get_category(db: Session, category_id: int) -> Category:
    # Using query to fetch an category by ID
    category = db.query(Category).filter(Category.category_id == category_id).first()  # `get()` is deprecated
    if not category:
        raise DbnotFoundException
    return category

def create_category(db: Session, category_data: CategoryCreate) -> Category:
    # Using model_dump() to convert the Pydantic model to a dict and pass to Category model

    new_category = Category(
        category_name=category_data.category_name,
        category_picture_url=category_data.category_picture_url,
        category_description=category_data.category_description,
    
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category

def update_category(db: Session, category_id: int, category_data: CategoryUpdate) -> Category:
    # Get the category object to be updated
    category_being_updated = get_category(db, category_id)
    
    # Using model_dump() to get only the fields that were updated
    update_data = category_data.model_dump(exclude_unset=True)

    # Loop over the updated fields and update the category object
    for key, value in update_data.items():
        setattr(category_being_updated, key, value)

    db.commit()  # Commit the changes to the database
    db.refresh(category_being_updated)  # Refresh to get the updated object with new values
    
    return category_being_updated

def delete_category(db: Session, category_id: int) -> None:
    # Fetch the category object to be deleted
    category = get_category(db, category_id)
    
    db.delete(category)
    db.commit()  # Commit the delete operation

def get_categorys(db: Session)->  list[Category]:
        
        categorys = db.query(Category).all()
        return categorys