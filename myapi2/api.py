from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from crud import get_all_cars, create_car, get_car_info_by_id, update_car_info, delete_car_info
from database import get_db
from exceptions import CarInfoException
from schemas import Car, CreateAndUpdateCar, PaginatedCarInfo

router = APIRouter()

@cbv(router)
class Cars:
    session: Session = Depends(get_db)

    @router.get("/cars", response_model=PaginatedCarInfo)
    def list_car(self, limit: int = 10, offset: int = 0):
        cars_list = get_all_cars(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": cars_list}

        return response

    @router.post("/cars")
    def add_car(self, car_info: CreateAndUpdateCar):
        try:
            car_info = create_car(self.session, car_info)
            return car_info
        except CarInfoException as cie:
            raise HTTPException(**cie.__dict__)

@router.get("/cars/{car_id", response_model=Car)
def get_car_info(car_id: int, session: Session = Depends(get_db)):
    try:
        car_info = get_car_info_by_id(session, car_id)
        return car_info
    except CarInfoException as cie:
        raise HTTPException(**cie.__dict__)

@router.put("/cars/{car_id}", response_model=Car)
def update_car(car_id: int, new_info: CreateAndUpdateCar, session: Session = Depends(get_db)):
    try:
        car_info = update_car_info(session, car_id, new_info)
        return car_info
    except CarInfoException as cie:
        raise HTTPException(**cie.__dict__)

@router.delete("/cars/{car_id}")
def delete_car(car_id: int, session: Session = Depends(get_db)):
    try:
        return delete_car_info(session, car_id)
    except CarInfoException as cie:
        raise HTTPException(**cie.__dict__)