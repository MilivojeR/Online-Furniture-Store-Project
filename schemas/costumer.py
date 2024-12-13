from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class CostumerBase(BaseModel):
    costumer_first_name: str
    costumer_last_name: str
    costumer_email: EmailStr
    costumer_password: str  
    costumer_adress:str
    costumer_all_order_details: Optional[str] = ""  # Default to empty string
    costumer_total_points_acquired: int = 0  # Default to 0
    costumer_day_created: Optional[datetime] = None  # New field
    costumer_day_last_purchase: Optional[datetime] = None  # New field

    class Config:
        orm_mode = True  


class CostumerCreate(CostumerBase):
    class Config:
        orm_mode = True  # 


class CostumerUpdate(CostumerBase):
    costumer_first_name: Optional[str] = None
    costumer_last_name: Optional[str] = None
    costumer_email: Optional[EmailStr] = None
    costumer_password: Optional[str] = None  
    costumer_adress:Optional[str] = None
    costumer_all_order_details:Optional[str] = None
    costumer_total_points_acquired:Optional[int] = None
    costumer_day_created: Optional[datetime] = None
    costumer_day_last_purchase: Optional[datetime] = None

class Costumer(CostumerBase):
    costumer_id: int  

    class Config:
        orm_mode = True  



