

from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select

from exceptions import DbnotFoundException
from models.category import Category
from schemas.category import CategoryCreate, CategoryUpdate

def get_category(db: Session, category_id: int) -> Category:

    category = db.query(Category).filter(Category.category_id == category_id).first()  
    if not category:
        raise DbnotFoundException
    return category

def create_category(db: Session, category_data: CategoryCreate) -> Category:
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

    category_being_updated = get_category(db, category_id)
    update_data = category_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(category_being_updated, key, value)

    db.commit()  
    db.refresh(category_being_updated) 
    
    return category_being_updated

def delete_category(db: Session, category_id: int) -> None:

    category = get_category(db, category_id)   
    db.delete(category)
    db.commit()  

def get_categorys(db: Session)->  list[Category]:
        
        categorys = db.query(Category).all()
        return categorys