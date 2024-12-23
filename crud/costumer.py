

from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime, timedelta
from exceptions import DbnotFoundException
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException,Depends

from models.admin import Admin
from models.costumer import Costumer
from schemas.costumer import CostumerCreate, CostumerUpdate


from crud.token import get_current_user_email

def get_costumer_by_id(db: Session, costumer_id: int) -> Costumer:
    # Using query to fetch an costumer by ID
    costumer = db.query(Costumer).filter(Costumer.costumer_id == costumer_id).first()  # `get()` is deprecated
    if not costumer:
        raise DbnotFoundException
    return costumer






def get_costumers(db: Session)->  list[Costumer]:
        
        costumers = db.query(Costumer).all()
        return costumers




#kreira korisnika i gleda dal postoji email unutar baze podataka takodje prolazi kroz emaile admina
#prilikom kreiranja hashuje password
def create_costumer(db: Session, costumer_data: CostumerCreate) -> Costumer:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_context.hash(costumer_data.costumer_password)
    admin_with_email = db.query(Admin).filter(Admin.admin_email == costumer_data.costumer_email).first()
    if admin_with_email:
        raise HTTPException(
            status_code=400, 
            detail="Email address is already in use"
        )

    else:
        try:  
            new_costumer = Costumer(
                costumer_first_name=costumer_data.costumer_first_name,
                costumer_last_name=costumer_data.costumer_last_name,
                costumer_email=costumer_data.costumer_email,
                costumer_adress=costumer_data.costumer_adress,
                costumer_all_order_details=costumer_data.costumer_all_order_details,
                costumer_total_points_acquired=costumer_data.costumer_total_points_acquired,
                costumer_password=hashed_password,  
                costumer_day_last_purchase=None,
                costumer_role=costumer_data.costumer_role
                )
            db.add(new_costumer)
            db.commit()
            db.refresh(new_costumer)
        except IntegrityError as e:

            db.rollback()
      
            raise HTTPException(
                status_code=400, 
                detail="Email address is already in use."
        )  
    return new_costumer

def update_costumer(db: Session, costumer_id: int, costumer_data: CostumerUpdate) -> Costumer:

    costumer_being_updated = get_costumer_by_id(db, costumer_id)
    if not costumer_being_updated:
        raise DbnotFoundException("Costumer not found, check id and enter another one!")
    update_data = costumer_data.model_dump(exclude_unset=True)


    #hash passworda
    if "costumer_password" in update_data:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        update_data["costumer_password"] =pwd_context.hash(costumer_data.costumer_password)

    #provjera dal postoji email u obje tabele Admin i Costumer
    admin_with_email = db.query(Admin).filter(Admin.admin_email == costumer_data.costumer_email).first()
    costumer_with_email = db.query(Costumer).filter(Costumer.costumer_email == costumer_data.costumer_email).first()



    #Ako postoji digni gresku
    if admin_with_email or costumer_with_email:
            raise HTTPException(
                status_code=400, 
                detail="Email address is already in use"
            )

    else: 
        #Ako ne postoji izvrsi update
        try:
            for key, value in update_data.items():
                setattr(costumer_being_updated, key, value)

            db.commit()  # Commit the changes to the database
            db.refresh(costumer_being_updated)  # Refresh to get the updated object with new values
            
        except IntegrityError as e:

            db.rollback()
      
            raise HTTPException(
                status_code=400, 
                detail="Email address is already in use."
        )  
    return costumer_being_updated



def update_current_costumer(db: Session, costumer_email: str, costumer_data: CostumerUpdate) -> Costumer:
    # Fetch the customer using the provided email


    costumer = db.query(Costumer).filter(Costumer.costumer_email == costumer_email).first()
    
    if not costumer:
        raise DbnotFoundException("Customer not found, check the email and enter another one!")
    
    update_data = costumer_data.model_dump(exclude_unset=True)

    # Hash password if it is included in the update
    if "costumer_password" in update_data:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        update_data["costumer_password"] = pwd_context.hash(costumer_data.costumer_password)

    # Check if the email exists in both Admin and Costumer tables
    admin_with_email = db.query(Admin).filter(Admin.admin_email == costumer_data.costumer_email).first()
    costumer_with_email = db.query(Costumer).filter(Costumer.costumer_email == costumer_data.costumer_email).first()

    # If email exists in either Admin or Costumer tables, raise an error
    if admin_with_email or (costumer_with_email and costumer_with_email.costumer_id != costumer.costumer_id):
        raise HTTPException(
            status_code=400,
            detail="Email address is already in use"
        )

    # Perform the update
    try:
        for key, value in update_data.items():
            setattr(costumer, key, value)

        db.commit()  # Commit changes to the database
        db.refresh(costumer)  # Refresh to get the updated object with new values
        
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Email address is already in use."
        )  

    return costumer



















def delete_costumer(db: Session, costumer_id: int) -> None:
    # Fetch the costumer object to be deleted
    costumer = get_costumer_by_id(db, costumer_id) 
    db.delete(costumer)
    db.commit()
