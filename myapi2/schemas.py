from pydantic import BaseModel
from model import FuelType
from typing import Optional, List

class CreateAndUpdateCar(BaseModel):
    manufacturer: str
    modelName: str
    cc: int
    onRoadPrice: int
    seatingCapacity: int
    gearbox: int
    fuelType: FuelType

class Car(CreateAndUpdateCar):
    id: int

    class Config:
        orm_mode = True

class PaginatedCarInfo(BaseModel):
    limit: int
    offset: int
    data: List[Car]