
import crud.costumer as costumers 
from schemas.costumer import  CostumerCreate,CostumerUpdate,CostumerBase,Costumer
from exceptions import DbnotFoundException
from database import db

from typing import Annotated
from fastapi import APIRouter, HTTPException, Query
router = APIRouter(prefix="/costumer", tags=["costumer"])

@router.get("/last-month", response_model=list[Costumer])
def get_last_month_new_costumers( db: db):
    try:
        return costumers.get_last_month_new_costumers(db)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Not any new costumer in last month  found!")

@router.get("/last-year", response_model=list[Costumer])
def get_last_year_new_costumers( db: db):
    try:
        return costumers.get_last_year_new_costumers(db)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Not any new costumer in last month  found!")










@router.get("/{costumer_id}", response_model=Costumer)
def get_costumer(costumer_id: int, db: db):
    try:
        return costumers.get_costumer(db, costumer_id)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Costumer {costumer_id} not found!")

@router.get("/", response_model=list[Costumer])
def get_costumers( db: db):
    try:
        return costumers.get_costumers(db)
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Not any costumers found!")







@router.post("", response_model=CostumerCreate, status_code=201)
def create_costumer(costumer:CostumerCreate, db: db):
    costumer = costumers.create_costumer(db, costumer)
    db.commit()
    db.refresh(costumer)
    return costumer


@router.put("/{costumer_id}", response_model=CostumerUpdate)
def update_costumer(costumer_id: int, costumer: CostumerUpdate, db: db):
    try:
        costumer = costumers.update_costumer(db, costumer_id, costumer)
        db.commit()
        db.refresh(costumer)
        return costumer
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Costumer {costumer_id} not found!")


@router.delete("/{costumer_id}", status_code=204)
def delete_costumer(costumer_id: int, db: db):
    try:
        costumers.delete_costumer(db, costumer_id)
        db.commit()
    except DbnotFoundException:
        raise HTTPException(status_code=404, detail=f"Costumer {costumer_id} not found!")

