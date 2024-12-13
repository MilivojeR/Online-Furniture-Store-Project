

from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime, timedelta
from exceptions import DbnotFoundException
from models.costumer import Costumer
from schemas.costumer import CostumerCreate, CostumerUpdate

def get_costumer(db: Session, costumer_id: int) -> Costumer:
    # Using query to fetch an costumer by ID
    costumer = db.query(Costumer).filter(Costumer.costumer_id == costumer_id).first()  # `get()` is deprecated
    if not costumer:
        raise DbnotFoundException
    return costumer

def get_costumers(db: Session)->  list[Costumer]:
        
        costumers = db.query(Costumer).all()
        return costumers

def get_last_month_new_costumers(db: Session) -> list[Costumer]:
    # Calculate start and end dates of the last month
    current_date = datetime.now()
    first_day_of_this_month = current_date.replace(day=1)
    last_day_of_last_month = first_day_of_this_month - timedelta(days=1)
    first_day_of_last_month = last_day_of_last_month.replace(day=1)

    # Query database for customers created last month
    costumers = db.query(Costumer).filter(
        Costumer.costumer_day_created >= first_day_of_last_month,
        Costumer.costumer_day_created <= last_day_of_last_month
    ).all()

    return costumers if costumers else []  # Return empty list

def get_last_year_new_costumers(db: Session) -> list[Costumer]:
    # Get the current year
    current_datetime = datetime.now()
    current_year = current_datetime.year

    # Calculate the start and end of the previous year
    start_of_last_year = datetime(current_year - 1, 1, 1)  # January 1st of last year
    end_of_last_year = datetime(current_year - 1, 12, 31, 23, 59, 59)  # December 31st of last year

    # Query all customers created in the previous year
    costumers = db.query(Costumer).filter(
        Costumer.costumer_day_created >= start_of_last_year,
        Costumer.costumer_day_created <= end_of_last_year
    ).all()
    
    return costumers if costumers else [] 






def create_costumer(db: Session, costumer_data: CostumerCreate) -> Costumer:
    # Using model_dump() to convert the Pydantic model to a dict and pass to Costumer model

    new_costumer = Costumer(
        costumer_first_name=costumer_data.costumer_first_name,
        costumer_last_name=costumer_data.costumer_last_name,
        costumer_email=costumer_data.costumer_email,
        costumer_adress=costumer_data.costumer_adress,
        costumer_all_order_details=costumer_data.costumer_all_order_details,
        costumer_total_points_acquired=costumer_data.costumer_total_points_acquired,
        costumer_password=costumer_data.costumer_password,
        costumer_day_last_purchase=None
    )





    db.add(new_costumer)
    db.commit()
    db.refresh(new_costumer)

    return new_costumer

def update_costumer(db: Session, costumer_id: int, costumer_data: CostumerUpdate) -> Costumer:
    # Get the costumer object to be updated
    costumer_being_updated = get_costumer(db, costumer_id)
    
    # Using model_dump() to get only the fields that were updated
    update_data = costumer_data.model_dump(exclude_unset=True)

    # Loop over the updated fields and update the costumer object
    for key, value in update_data.items():
        setattr(costumer_being_updated, key, value)

    db.commit()  # Commit the changes to the database
    db.refresh(costumer_being_updated)  # Refresh to get the updated object with new values
    
    return costumer_being_updated

def delete_costumer(db: Session, costumer_id: int) -> None:
    # Fetch the costumer object to be deleted
    costumer = get_costumer(db, costumer_id)
    
    db.delete(costumer)
    db.commit()  # Commit the delete operation