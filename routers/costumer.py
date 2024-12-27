from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from exceptions import DbnotFoundException

from crud.token import check_admin_role,check_customer_role
from schemas.costumer import Costumer, CostumerCreate, CostumerUpdate
from database import get_db 
import crud.costumer as costumers
from crud.token import get_current_user_email
from schemas.token import TokenData

router = APIRouter()

# Public endpoint: Fetch all customers
@router.get("/costumers", response_model=list[Costumer],dependencies=[Depends(check_admin_role)], tags=["admin-only"])
def get_costumers(db: Session = Depends(get_db)):
    try:
        return costumers.get_costumers(db)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail="No customers found!")

# Admin-only endpoint: Fetch a single customer by ID
@router.get("/costumers/{costumer_id}", response_model=Costumer, dependencies=[Depends(check_admin_role)], tags=["admin-only"])
def get_costumer(costumer_id: int, db: Session = Depends(get_db)):
    try:
        return costumers.get_costumer_by_id(db, costumer_id)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Customer {costumer_id} not found!")

# Customer-only endpoint: Create a new customer
@router.post("/costumers/create", response_model=CostumerCreate, status_code=201, tags=["public"])
def create_costumer(costumer: CostumerCreate, db: Session = Depends(get_db)):
    costumer = costumers.create_costumer(db, costumer)
    return costumer
# Admin-only endpoint: Delete a customer
@router.delete("/costumers/{costumer_id}", status_code=204, dependencies=[Depends(check_admin_role)], tags=["admin-only"])
def delete_costumer(costumer_id: int, db: Session = Depends(get_db)):
    try:
        costumers.delete_costumer(db, costumer_id)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Customer {costumer_id} not found!")

# Admin-only endpoint: Update a customer's details
@router.put("/costumers/{costumer_id}", response_model=CostumerUpdate, dependencies=[Depends(check_admin_role)], tags=["admin-only"])
def update_costumer(costumer_id: int, costumer: CostumerUpdate, db: Session = Depends(get_db)):
    try:
        costumer = costumers.update_costumer(db, costumer_id, costumer)
        return costumer
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Customer {costumer_id} not found!")
    
#Costumer only endpoint: Self update
@router.put("/costumers-only/", response_model=CostumerUpdate, dependencies=[Depends(check_customer_role)], tags=["costumer_only"])
def update_current_costumer( costumer: CostumerUpdate,costumer_email: str = Depends(get_current_user_email),  db: Session = Depends(get_db)):
    
    try:
        costumer = costumers.update_current_costumer(db, costumer_email,costumer)
        return costumer
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"To upgrade login with new  credentials")
    
