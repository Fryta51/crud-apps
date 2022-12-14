from typing import List
from sqlalchemy.orm import Session
from exceptions import CarInfoNotFoundError, CarInfoInfoAlreadyExistError
from model import CarInfo
from schemas import CreateAndUpdateCar

def get_all_cars(session: Session, limit: int, offset: int) -> List[CarInfo]:
    return session.query(CarInfo).offset(offset).limit(limit).all()

def get_car_info_by_id(session: Session, _id: int) -> CarInfo:
    car_info = session.query(CarInfo).get(_id)

    if car_info is None:
        raise CarInfoNotFoundError
    
    return car_info

def create_car(session: Session, car_info: CreateAndUpdateCar) -> CarInfo:
    car_details = session.query(CarInfo).filter(CarInfo.manufacturer == car_info.manufacturer, CarInfo.modelName == car_info.modelName).first()
    if car_details is not None:
        raise CarInfoInfoAlreadyExistError
    
    new_car_info = CarInfo(**car_info.dict())
    session.add(new_car_info)
    session.commit()
    session.refresh(new_car_info)
    return new_car_info

def update_car_info(session: Session, _id: int, info_update: CreateAndUpdateCar) -> CarInfo:
    car_info = get_car_info_by_id(session, _id)

    if car_info is None:
        raise CarInfoNotFoundError

    car_info.manufacturer = info_update.manufacturer
    car_info.modelName = info_update.modelName
    car_info.fuelType = info_update.fuelType
    car_info.cc = info_update.cc
    car_info.gearbox = info_update.gearbox
    car_info.onRoadPrice = info_update.onRoadPrice
    car_info.seatingCapacity = info_update.seatingCapacity

    session.commit()
    session.refresh(car_info)

    return car_info

def delete_car_info(session: Session, _id: int):
    car_info = get_car_info_by_id(session, _id)

    if car_info is None:
        raise CarInfoNotFoundError

    session.delete(car_info)
    session.commit()

    return