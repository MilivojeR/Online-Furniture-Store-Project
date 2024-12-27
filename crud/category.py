from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select

from exceptions import DbnotFoundException
from models.category import Category
from schemas.category import CategoryCreate, CategoryUpdate

#get category by id
def get_category(db: Session, category_id: int) -> Category:

    category = db.query(Category).filter(Category.category_id == category_id).first()  # `get()` is deprecated
    if not category:
        raise DbnotFoundException
    return category

#create category
def create_category(db: Session, category_data: CategoryCreate) -> Category:
    # create new category with constructor
    new_category = Category(
        category_name=category_data.category_name,
        category_picture_url=category_data.category_picture_url,
        category_description=category_data.category_description,
    
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

#update category by id
def update_category(db: Session, category_id: int, category_data: CategoryUpdate) -> Category:
    # Get the category object to be updated
    category_being_updated = get_category(db, category_id)
    update_data = category_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(category_being_updated, key, value)

    db.commit()  
    db.refresh(category_being_updated)  
    
    return category_being_updated

#delete category
def delete_category(db: Session, category_id: int) -> None:
    # Fetch the category object to be deleted
    category = get_category(db, category_id)
    db.delete(category)
    db.commit()  # Commit the delete operation

#list all the categories
def get_categorys(db: Session)->  list[Category]:
        
        categorys = db.query(Category).all()
        return categorys